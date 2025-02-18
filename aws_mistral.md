# LIST OF STEPS
[Go to RUN OPEN WEBUI IN EC2](#run-open-webui-in-ec2) \
[Go to STEP INITIALIZE AWS INSTANCE](#STEP-INITIALIZE-AWS-INSTANCE) \

## Initialize AWS Instance and cluster
### Create an EKS Cluster using eksctl
```
eksctl create cluster --name openwebui-cluster --region us-east-1 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 2 \
  --nodes-max 5 \
  --managed

```

## vLLM Deployment (Private, Only Accessible by Open WebUI)
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm
spec:
  replicas: 1
  selector:
    matchLabels:
      app: vllm
  template:
    metadata:
      labels:
        app: vllm
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        args:
          - "--model"
          - "/models/mistral-7B"
        resources:
          limits:
            nvidia.com/gpu: 1
        volumeMounts:
          - name: model-storage
            mountPath: /models
      volumes:
        - name: model-storage
          hostPath:
            path: /models
---
apiVersion: v1
kind: Service
metadata:
  name: vllm-service
spec:
  selector:
    app: vllm
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  type: ClusterIP  # ❗ This keeps vLLM private within the cluster

```

## Open WebUI yaml Deployment (Publicly Accessible, Talks to vLLM Internally)
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openwebui
spec:
  replicas: 1
  selector:
    matchLabels:
      app: openwebui
  template:
    metadata:
      labels:
        app: openwebui
    spec:
      containers:
      - name: openwebui
        image: open-webui/open-webui:latest
        env:
          - name: OLLAMA_BASE_URL
            value: "http://vllm-service:8000"  # ❗ Connect to vLLM inside cluster
        ports:
          - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: openwebui-service
spec:
  selector:
    app: openwebui
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer  # ❗ Exposes Open WebUI to external users or Ingress
```

## STEP INITIALIZE AWS INSTANCE 

## STEP SSH / CLI AND CHECK NVIDIA INSTALLATION

## STEP INSTALL DOCKER-COMPOSE

## STEP INSTALL DOCKER ON EC2
in ssh, run:
```
sudo apt update && sudo apt install -y docker.io docker-compose
sudo systemctl enable --now docker
```

## RUN OPEN WEBUI IN EC2
```
docker run -d --name open-webui \
  -p 3000:3000 \
  -e OPENAI_API_BASE_URL=http://<EC2-PUBLIC-IP>:8000/V1 \
  -v open-webui-date:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

## ACCESS OPEN WEBUI
```
http://<EC2-PUBLIC-IP>:3000
```

## RESOURCES
DOCKER-COMPOSE YAML FOR WEB-UI
(https://www.linkedin.com/pulse/step-by-step-launching-ollama-server-web-ui-amazon-ec2-emesoft-jsc-0oc6c)

SECURE HTTPS CONNECTION, HEALTH CHECKS
(https://aws.plainenglish.io/deploying-deepseek-r1-on-ecs-fargate-with-open-webui-a-scalable-ollama-ai-solution-0008049a73a9)

USE DOMAIN NAME, REVERSER PROXY W/ NGINX AND SECURE WITH SSL (SEE CGPT)

### MOUNT LOCAL LLM INTO CONTAINER AND INSTRUCT vLLM TO LOAD MODEL FROM LOCAL DIR, USING HOST'S IPC NAMESPACE, HENCE SHARED MEM INSTEAD OF DEFAULT ISOLATED IPC NAMESPACE/MEM, RUN ON PORT 8000
```
docker run --runtime=nvidia --gpus=all \
  -v ~/models/mistral-7b:/model \
  -p 8000:8000 \
  --ipc=host \
  vllm/vllm-openai:latest \
  --model /model
```
### K8s example YAML template

### THOUGHTS
1. EC2 Auto Scaling adjusts the # of running instances based on metrics while
   HPA scales pods in the instance nodes
   1a. w/ Elastic Load Balancer(ELB), ensures traffic is routed correctly.
       to all available instances.
3. Auto stopping instances may have to use AWS Lambda and CloudWatch.
4. Set up API Gateway to handle HTTP requests to Lambda functions, which can ensure
   that EC2 instances only start when Lambda function get triggered and run.
5. AWS CloudFront is a CDN that can cache content closesr to users.
   Used for static content (e.g, HTML, JS, images) and only charges for traffic.


### run Open WebUI with Docker
``` docker run -d --name open-webui \
  -p 3000:3000 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:8000/v1 \
  -v open-webui-data:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```
add command -e OPENAI_API_KEY=dummy-key to set default API key for all users.
or 
modify file if running without docker, eg writing yaml



## STEP GET MISTRAL INSTRUCT AND INFER

1. under mistral-ai tutorials: (https://github.com/mistralai/mistral-inference/blob/main/tutorials/getting_started.ipynb) \
   (https://colab.research.google.com/github/mistralai/mistral-inference/blob/main/tutorials/getting_started.ipynb)
   from how to run (https://docs.mistral.ai/getting-started/models/weights/#how-to-run)
or
3. via HF
(https://chatgpt.com/c/67a8c887-3254-8013-866b-3ce0b0aefd07)
```
  git lfs install
  git clone https://huggingface.co/mistralai/Mistral-7B-v0.1 ~/models/mistral-7b
```
more ideas in case of multiple version, delete to save space
(https://stackoverflow.com/questions/67595500/how-to-download-a-model-from-huggingface) \
(https://www.youtube.com/watch?v=1lC0GQtAz1s) \
HF transformer main page also shows git clone transfomer w/o need of account

## quantization quick start with vLLM
https://docs.mistral.ai/getting-started/models/weights/#how-to-run


