###
#
# 28 jan 2025 afternoon, i have some ideas and links
# to iterate, to mostly use AWS console
# so I can understand the basics visually what AWS has to offer
# before I switch to terraform to gain the blueprints to scale
# 
# source 1:  https://medium.com/@chinmayd49/self-host-llm-with-ec2-vllm-langchain-fastapi-llm-cache-and-huggingface-model-7a2efa2dcdab
#   - running ec2 thru console
#   - start time and end time code for latency
# source 2:  nlp cloud - deploy the Mistral 7b Gen model on an A10 GPU on AWS 
#   - aws console, mistral 7b, 
# source 2a: simpler form from nlpcloud, just pip vLLM, could ignore ray and no HF
#   - https://nlpcloud.com/deploy-llama-2-mistral-and-mixtral-on-aws-ec2-with-vllm.html,


# misc: 
# - eksctl delete cluster my-demo-cluster --region us-east-1 by mudasir - setup k8s cluster on EKS (shows how to create cluster n node)
# - self-host llama 3.1 88B in EC2 using VLLM and Docker by Mohamed Amri show good example of setup by console
# - "If you already have the model artifacts on your infrastructure you can use them directly by pointing vLLM to their local path 
#    instead of a Hugging Face model ID. 
#    In this scenario you will be able to skip all Hugging Face related setup steps."
#   https://docs.mistral.ai/deployment/self-deployment/vllm/
# - also see prod metrics and distributed inference and serving on vLLM official docs

# - https://www.reddit.com/r/MachineLearning/comments/1apxg42/d_deploy_mixtral_8x7b_llama_2_and_mistral_on_aws/
#   link above provides additional idea for compute, latency n request rate costs.

# so I need to download vLLM and mistral to cloud via SSH, if not from HF, and point to the mistral path like this LLM("/mistral/path")

##### conclusion #####
##  algo:
##  1) follow nlpcloud first
##  2) check ssh from chinmay
##  3) download mistral and vllm (nlpcloud)
##  4) point to directory and test generation
##  5) terminate EC2 isntance (or eksctl delete cluster)
##
##  so we would've learnt to configure ec, install vLLM and OS model for personal usage 
##  then we will understand better how to scale better for prod using EKS (from console->CLI/SSH?), Load Balancers and FastAPI
##  (see other tutorials like vic Gu's for arch and add. (AWS) services, articles that uses eks console eg mudasir, to aws workshop schema)

## our app will probably end up like Gu and aws workshop schema, where the entry(endpoints) would be the UIs such as login, transcript and translate page
## for the AI apps to process and return the data to the appropriate features on certain pages, such as the page with embedded utube vid with overlayed subs.
#####
# It would be similar to reinventing the internet/WWW, creating my own personal network and allowing specific communication from different categories of people
###

##############################################
###############################################
## 8 feb, 2025, Sat
##########################
#
# from 0900 - 1330
# reviewed materials accrued to be implemented and wrote in slides "Mistral on aws"
# if all goes well, we need to open an S3 or EBS monthly to store model, script
# to be loaded on ec2 instance. 
#
# need to link to web openUI if I want to access via web interface.
#
# 
