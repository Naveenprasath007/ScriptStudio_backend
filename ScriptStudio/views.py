from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ScriptStudio.serializers import scriptSerializer
from ScriptStudio.models import scripts


from dotenv import load_dotenv
load_dotenv()
import openai
import os
import uuid 
  



@csrf_exempt
def scriptApi(request,id=0):
    if request.method=='GET':
        script = scripts.objects.all()
        script_serializer=scriptSerializer(script,many=True)
        return JsonResponse(script_serializer.data,safe=False)
    
    elif request.method=='POST':
        script_data=JSONParser().parse(request)
        print("TEST",script_data)
        script_serializer=scriptSerializer(data=script_data)
        if script_serializer.is_valid():
            script_serializer.save()
            print("saved")
            return JsonResponse("Added Successfully",safe=False)
        print("failed")
        return JsonResponse("Failed to Add",safe=False)
    
    elif request.method=='PUT':
        script_data=JSONParser().parse(request)
        script=scripts.objects.get(scripts_id=id)
        script_serializer=scriptSerializer(script,data=script_data)
        if script_serializer.is_valid():
            script_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        script=scripts.objects.get(id=id)
        script.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt
def generate(request):
        if request.method == "POST":
            id = uuid.uuid4() 
            print(id)
            data=JSONParser().parse(request)
            input=data.get("prompt")
            print(input)
            result=scriptgenerate(input)
            paragraphs = result.split('\n\n')

            # Print individual paragraphs
            for i, paragraph in enumerate(paragraphs, start=1):
                if i == 1:
                    paragraph1=paragraph
                elif i == 2:
                    paragraph2=paragraph
                elif i == 3:
                    paragraph3=paragraph
                elif i == 4:
                    paragraph4=paragraph
                elif i == 5:
                    paragraph5=paragraph


            script={"scripts_id":str(id),"paragraph1":paragraph1,"paragraph2":paragraph2,"paragraph3":paragraph3,"paragraph4":paragraph4,"paragraph5":paragraph5}
            
            dict3 = Merge(data, script)
            print(dict3)
            script_serializer=scriptSerializer(data=dict3)
            if script_serializer.is_valid():
                script_serializer.save()
            else:
                 print("NOT WORKING")

            return JsonResponse(script)   
        else:
            msg = "Hi Hello"
            return JsonResponse("Fetching backend data successfully",safe=False)




# Python code to merge dictionary
def Merge(dict1, dict2):
	for i in dict2.keys():
		dict1[i]=dict2[i]
	return dict1
	



@csrf_exempt
def scriptgenerate(input):
    number_of_text=5
    openai.api_key = os.getenv('api_key')
    prompt = f"Create a {number_of_text} different content for compelling advertisement for {input} that highlights its unique features and benefits. Emphasize why customers should choose Particular {input} over competitors. Use persuasive language and give the output in one single paragraph for each"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will be provided with the topics and create the text content for the topic."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=750,
    )

    result = completion.choices[0].message.content   
    return result
