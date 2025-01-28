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
# - "If you already have the model artifacts on your infrastructure you can use them directly by pointing vLLM to their local path instead of a Hugging Face model ID. 
# -  In this scenario you will be able to skip all Hugging Face related setup steps."
#   https://docs.mistral.ai/deployment/self-deployment/vllm/
# - also see prod metrics and distributed inference and serving on vLLM official docs

# - https://www.reddit.com/r/MachineLearning/comments/1apxg42/d_deploy_mixtral_8x7b_llama_2_and_mistral_on_aws/
#   link above provides additional idea for compute, latency n request rate costs.

# so I need to download vLLM and mistral to cloud via SSH, if not from HF, and point to the mistral path like this LLM("/mistral/path")

##### conclusion #####
##  follow nlpcloud first
##  check ssh from chinmay
##  download mistral and vllm (nlpcloud)
##  point to directory and test generation
##  terminate EC2 isntance (or eksctl delete cluster)
##
##  so we would've learnt to configure ec, install vLLM and OS model for personal usage 
##  then we will understand better how to scale better for prod using EKS, Load Balancers and FastAPI
##  (see other tutorials like vic Gu's for arch and add. (AWS) services, articles that uses eks console eg mudasir, to aws workshop schema)
