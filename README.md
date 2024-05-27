# LambdaPolly
Use of Polly with lambda 

Install 

```python


pip install requests
```
## Lambda Polly

- **Function:** The Lambda Polly function includes a base64 text encoding feature.
- **Description:** This Lambda function accepts text input, synthesizes it into speech using Amazon Polly, and returns the synthesized audio file as a base64-encoded MP3.
- **Lambda Function URL:** [Insert URL here]

## lambdapolly.py

- **Description:** This Python script sends a request to the Lambda Polly function. Before sending the request, it prompts the user to input a word or phrase. Subsequently, it transmits this input to the Lambda function, retrieves the synthesized audio file, and saves it as an MP3 file.
- **How to Use:** Execute the `lambdapolly.py` script and follow the prompts to input the desired word or phrase for synthesis.
- **Requirements:** Ensure Python is installed along with the `requests` and `base64` libraries.
- **Usage Example:**
  ```bash
  python lambdapolly.py
  ```

![image](https://github.com/anthonycs4/LambdaPolly/assets/165516654/989653ef-3195-457c-9d3c-52a1a52ff47c)
![image](https://github.com/anthonycs4/LambdaPolly/assets/165516654/f2db27bf-e2a8-4878-96ee-6a19d0ea53c9)

  


