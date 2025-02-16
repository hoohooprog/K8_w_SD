source: https://nlpcloud.com/deploy-mistral-7b-on-a10-gpu-on-aws.html

background:
- Mistral7b requires at least 15GB of VRAM, so we need at least 1xA10GPU
- 1xA10GPU = edit: 24gb of GPU
- in Amazon, g5.xlarge instance uses 


algo:
1) goto aws management console
2) goto EC2 dashboard
3) click `launch instance`
4) choose ubuntu server
5) select `deep learning ami gpu pytorch` preferred version/release date
6) why not x1? because 7b needs at least 14GB of staging mem, may be tight, so maybe x2?
7) g5x2 has 32gb ram instead of 16gb ram of g5x1, so I selected this to try
8) write name `mistral_g5x2_RAM16GB_A10GPU_24GB
9) 

## 15 feb 2025
https://github.com/open-webui/open-webui/tree/main/kubernetes/manifest/base
https://github.com/vllm-project/vllm/blob/367cb8ce8c0486e22941cf8990902fc5ec992ec1/docs/source/deployment/k8s.md

we have some sources for k8s thanks to CGPT. But CGPT does it differently. Maybe I should start executing soon
So I can have a sandbox to keep modifying and layering on, such as security etc.

- 2210
my intuition is, Open WebUI could be mainly svelte, hence JS/static file, and these are sent to users.
CDN etc, 
hence the real part that has to scale would be vLLM-Mistral, which is called by the Open WebUI service.

- 2216
So i Went thru EKS workshop on autoscaling, and verified the fact that EKS can be configured to autoscale nodes also
However, I would want scaling Open WebUI based on traffic latency ie LoadBalancing while vLLM on Compute.

## 16 feb 2025
- 1432, after break 12-1300, and before was doing reading on yaml files for k8 and port and pods scaling with LoadBalancers.
- we can see that our eks deployment is like DMV. we have a interface for users to select media,
  to be translated and returned by a machine (hidden operation).
  
  Then, User can choose to go to counter(s) for customer service agents with their respective tickets,
  or returning users can also go to the agents to find out about existing tickets.

  The supervising managers of the firm(instance) or departments(pods) decide if more access(ports) should be placed,
  more agents(containers) should be used and the criteria upon which traffic should be directed.
  And with regards to access, which are publicly accessible to users, and which are interdepartmental access only.

  the managers (Karpenter-trained?) decide additions or subtractions based on metrics provided.

  We also have the machines that the department uses (eg vLLM employs mistral7b v0.3 model).

  potentially shutdown and opening (node termination, starting by lambda worker).

  Hence 1 way of building would be to start from the core services, test them for traffic handling capabilities,
  and then open doors to public. Well, it's easier to evolve any platform on the web anyways.
  
  
