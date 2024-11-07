from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io

@csrf_exempt
def bw_image(request):
  print("Request received")
  if request.method == 'POST' and request.FILES.get('image'):
    uploaded_image = request.FILES['image']
    image = Image.open(uploaded_image)
    bw_image = image.convert('1')
    buffer = io.BytesIO()
    bw_image.save(buffer, 'JPEG')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/jpeg')
  
  return HttpResponse("Please upload an image", status=400)