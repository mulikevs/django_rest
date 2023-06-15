import logging
from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from django.http.response import JsonResponse
from rest_framework.decorators import (
    authentication_classes,
    permission_classes,
    api_view,
)

from BlogPost.models import Blog, Comments
from BlogPost.serializers import BlogSerializer, CommentSerializer
from django.core.files.storage import default_storage


logger = logging.getLogger(__name__)


@csrf_exempt
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def UsersAPIView(request):
    try:
        return JsonResponse({"status": "success", "message": str(request.user)}, status=200)
    except ValidationError as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=200  )



@csrf_exempt
@api_view(["GET"])
def blogApiGet(request, id=0):
    blogs = Blog.objects.all()
    blog_serializer = BlogSerializer(blogs, many=True)
    logger.info("GET request received for blogs")
    return JsonResponse({"status": "success", "data": blog_serializer.data}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([BasicAuthentication])
def blogApiPost(request, id=0):
    blog_data = JSONParser().parse(request)
    blog_serializer = BlogSerializer(data=blog_data)
    if blog_serializer.is_valid():
        try:
            blog_serializer.save()
            logger.info("POST request received for adding a blog")
            return JsonResponse(
                {"status": "success", "message": "Added Successfully!"}, status=201
            )
        except ValidationError as e:
            logger.error("Blog already exists")
            return Response({"status": "error", "message": e.args[0]}, status=400)
    logger.error("Invalid data received in POST request for adding a blog")
    return Response({"status": "error", "message": "Invalid data."}, status=400)


@csrf_exempt
def blogDetailApi(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Blog does not exist."}, safe=False
        )

    if request.method == "GET":
        blog_serializer = BlogSerializer(blog)
        return JsonResponse(
            {"status": "success", "data": blog_serializer.data}, status=200
        )
    elif request.method == "PUT":
        blog_data = JSONParser().parse(request)
        blog_serializer = BlogSerializer(blog, data=blog_data)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse(
                {"status": "success", "message": "Updated Successfully!"}, status=200
            )
        return JsonResponse(
            {"status": "error", "message": "Failed to Update."}, status=400
        )
    elif request.method == "DELETE":
        blog.delete()
        return JsonResponse(
            {"status": "success", "message": "Deleted Successfully!"}, status=200
        )


@csrf_exempt
def blogLikeApi(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Blog does not exist."}, safe=False
        )

    if request.method == "PUT":
        blog_data = JSONParser().parse(request)
        if "bloglikes" in blog_data:
            blog.bloglikes += blog_data["bloglikes"]
        if "blogdislikes" in blog_data:
            blog.blogdislikes += blog_data["blogdislikes"]
        blog.save()
        return JsonResponse(
            {"status": "success", "message": "Updated Successfully!"}, status=200
        )
    else:
        return JsonResponse(
            {"status": "error", "message": "Failed to Update."}, status=400
        )


@csrf_exempt
def add_comment(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Blog does not exist."}, safe=False
        )

    if request.method == "POST":
        comment_data = JSONParser().parse(request)
        comment_data["blog"] = blog.id
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(
                {"status": "success", "message": "Comment added successfully!"}
            )
        return JsonResponse(comment_serializer.errors, status=400)


@csrf_exempt
def get_comments(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Blog does not exist."}, safe=False
        )

    if request.method == "GET":
        comments = Comments.objects.filter(blog=blog)
        comment_serializer = CommentSerializer(comments, many=True)
        return JsonResponse({"status": "success", "data": comment_serializer.data})
    else:
        return JsonResponse(
            {"status": "error", "message": "Invalid request method."}, status=400
        )


@csrf_exempt
def SaveFile(request):
    file = request.FILES["file"]
    file_name = default_storage.save(file.name, file)
    return JsonResponse(
        {
            "status": "success",
            "message": "File added successfully!",
            "file_name": file_name,
        },
        safe=False,
    )
