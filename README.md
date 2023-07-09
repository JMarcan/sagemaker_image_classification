# Deploy and monitor a machine learning workflow for Image Classification

This project was part of my Machine Learning Nanodegree at Udacity.<br>
I used the AWS SageMaker to train and deploy the model<br>
together with event-driven inference workflow orchestrated via Step Function <br>
consisting of three lambda functions. <br><br>


**Step function workflow**

![Step Function Workflow](lambdas/inference-workflow.png "Step Function Workflow")

**Inference passing the threshold**
![Inference passing the threshold](assets/inference_successful_execution.png "Inference passing threshold")

**Inference not passing the threshold**
![Inference not passing the threshold](assets/inference_execution_not_passing_confidence_threshold.png "Inference not passing the threshold")
<br>
The model itself is trained on the CIFAR dataaset hosted by the University of Toronto<br>
to classify images of bikes and motorcycles

<br>
The SageMaker Model Monitor is used to observe the Endpoint<br>
so we can visualize and evaluate the inferences.<br><br>

**Model confidence for recent inferences**

![Model Confidence for recent Inferences](assets/Confidence_Threshold_Recent_Inferences.png "Model Confidence for recent Inferences")

**Visual inspection of recent inferences**
![Visual Inspection of recent inferences](assets/Visual_Inspection_Recent_Inferences.png "Visual inspection of recent inferences")
