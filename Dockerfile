FROM public.ecr.aws/lambda/python:3.9
COPY requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ${LAMBDA_TASK_ROOT}