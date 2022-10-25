FROM public.ecr.aws/lambda/python:3.8
WORKDIR /app 
COPY . /app
RUN pip3 install -r requirements.txt 

CMD ["app.handler"]