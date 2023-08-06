# alira

## Table of Contents

-   [Modules](#modules)
    -   [Map module](#map-module)
    -   [Selection module](#selection-module)
    -   [Flagging module](#flagging-module)
    -   [Dashboard module](#dashboard-module)
    -   [Email Notification module](#email-notification-module)
    -   [S3 module](#s3-module)
    -   [SocketIO module](#socketio-module)
-   [Implementing custom code](#implementing-custom-code) 
-   [Running the test suite](#running-the-test-suite)

## Modules

### Map module

You can use the Map module to apply a given function to every instance processed by the pipeline.

```yaml
name: thermal

pipeline:
- module: alira.modules.Map
    function: thermal.pipeline.map
```

The module expects a function with the following signature:

```python
def map(instance: Instance) -> dict:
    return {
        "hello": "world"
    }
```

The properties returned by the function will be automatically added to the instance as part of its `properties` dictionary under a key with the name of the function. For example, the above setup will add a `thermal.pipeline.map` key to the instance's `properties` dictionary containing the result of the function.

### Selection module

You can use the Selection module to select a percentage of instances as they go through the pipeline and flag them for human review. Having a group of instances reviewed by humans gives the model a baseline understanding of its performance, and allows it to compute metrics that can later be extrapolated to all processed instances.

```yaml
name: thermal

pipeline:
- module: alira.modules.selection.Selection
    percentage: 0.2
```

The above example will extend `instance.properties` with a new `selected` attribute under the `alira.modules.selection` key. The value of this attribute will be `1` if the instance has been selected for review, and `0` otherwise.

### Flagging module

You can use the Flagging module to optimize the decision of routing instances for human review.

There are two implementations of the Flagging module:

-   `alira.modules.flagging.Flagging`
-   `alira.modules.flagging.CostSensitiveFlagging`

#### `alira.modules.flagging.Flagging`

This implementation optimizes the decision of routing instances to a human using a threshold. Any instance with a confidence below the threshold will be sent for human review.

```yaml
name: thermal

pipeline:
- module: alira.modules.flagging.Flagging
    threshold: 0.7
```

This module will extend `instance.properties` with a new `alira.modules.flagging` key containing the attribute `flagged`. This attribute indicates whether the instance has been flagged for human review. This attribute is `1` if the instance has been flagged for review, and `0` otherwise.

#### `alira.modules.flagging.CostSensitiveFlagging`

This implementation uses cost sensitivity criteria to reduce the cost of mistakes.

```yaml
name: thermal

pipeline:
- module: alira.modules.flagging.CostSensitiveFlagging
    fp_cost: 100
    fn_cost: 1000
    human_review_cost: 10
```

When configuring the module, you can specify the following attributes:

-   `fp_cost` (`float`): The cost of a false positive prediction. This attribute is optional and when not specified the module will assume the cost is `0`.
-   `fn_cost` (`float`): The cost of a false negative prediction. This attribute is optional and when not specified the module will assume the cost is `0`.
-   `human_review_cost` (`float`): The cost sending this instance for human review. This attribute is optional and when not specified the module will assume the cost is `0`.

This module will extend `instance.properties` with a new `alira.modules.flagging` key containing the following attributes:

-   `flagged`: Whether the instance has been flagged for human review. This attribute is `1` if the instance has been flagged for review, and `0` otherwise.
-   `cost_prediction_positive`: The cost associated with a positive prediction.
-   `cost_prediction_negative`: The cost associated with a negative prediction.

### Dashboard module

You can use the Dashboard module to automatically extend every instance with a set of predefined user-friendly properties derived from the instance original attributes. The module also supports specifying a list of custom attribute:label pairs that will be added to the instance.

```yaml
name: thermal

pipeline:
- module: alira.modules.Dashboard
    attributes:
        confidence: This is the confidence
        metadata.temperature: Max Temperature
```

The above example will extend `instance.properties` with a dictionary under the `alira.modules.dashboard` key containing the following attributes:

-   `prediction`: A user-friendly value derived from the `instance.prediction` field.
-   `confidence`: A user-friendly value derived from the `instance.confidence` field.
-   `selected`: A user-friendly value derived from the `instance.properties["alira.modules.selection"]` field.
-   `flagged`: A user-friendly value derived from the `instance.properties["alira.modules.flagging"]` field.
-   `attributes`: A dictionary containing the list of custom attributes defined in the pipeline configuration. Each attribute added to this dictionary will have a `label` and a `value` property:
    -   `confidence`: The `value` will be the value of the `instance.confidence` field and the `label` will be `This is the confidence`.
    -   `metadata.temperature`: The `value` will be the value of the `instance.metadata["temperature"]` field and the `label` will be `Max Temperature`.

These new fields will be used by the Dashboard container to display every instance. If the Dashboard module is not included as part of a pipeline, the Dashboard container will not be available for this model.

### Email Notification module

You can use the Email Notification module to send email notifications to a list of email addresses. By default, this module uses AWS' Simple Email Service (SES) to send the notifications.

```yaml
name: thermal

pipeline:
- module: alira.modules.notification.EmailNotification
    filtering: alira.instance.onlyPositiveInstances
    sender: thermal@levatas.com
    recipients:
        - user1@levatas.com
        - user2@levatas.com
    subject: Random subject
    template_html_filename: template.html
    template_text_filename: template.txt
```

When configuring the module, you can specify the following attributes:

-   `filtering`: An optional function that will be used to filter instances to decide whether recipients should be notified about them. If this function is not specified, the instance will be included. For convenience purposes, there are two predefined functions that you can use:

    -   `alira.instance.onlyPositiveInstances`: Only positive instances will be notified.
    -   `alira.instance.onlyNegativeInstances`: Only negative instances will be notified.

-   `sender`: The email address of the sender of the email notification.
-   `recipients`: A list of email addresses that will be included in the email notification.
-   `subject`: The subject of the email notification.
-   `template_html_filename`: The name of the HTML template file that will be used to construct the email notification. This file should be located in the same directory as the pipeline configuration file.
-   `template_text_filename`: The name of the text template file that will be used to construct the email notification. This file should be located in the same directory as the pipeline configuration file.

### S3 module

You can use the S3 modiule to upload the image associated to an instance to S3.

```yaml
name: thermal

pipeline:
- module: alira.modules.s3.S3
    filtering: alira.instance.onlyPositiveInstances
    aws_s3_bucket: sample-bucket
    aws_s3_key_prefix: images
    aws_s3_public: true
```

When configuring the module, you can specify the following attributes:

-   `filtering`: An optional function that will be used to filter instances to decide whether the image should be uploaded to S3. If this function is not specified, the instance will be uploaded. For convenience purposes, there are two predefined functions that you can use:

    -   `alira.instance.onlyPositiveInstances`: Only the image from positive instances will be uploaded.
    -   `alira.instance.onlyNegativeInstances`: Only the image from negative instances will be uploaded.

-   `aws_s3_bucket`: The S3 bucket where the image will be stored.
-   `aws_s3_key_prefix`: The key prefix that will be used when storing this image in the S3 bucket.
-   `aws_s3_public`: Whether the image should be publicly accessible.

### SocketIO module

You can use the SocketIO module to send notifications to a socketio endpoint. This module is useful to combine with the Dashboard module so users can receive real time notifications every time an instance is processed.

```yaml
name: thermal

pipeline:
- module: alira.modules.notification.SocketIO
    endpoint: http://dashboard:3000/socketio
```

When configuring the module, you can specify the following attributes:

-   `endpoint`: The URL of the socketio endpoint that will receive the notification.

## Implementing custom code

Several modules require a function to do some sort of processing. For example, the [Map module](#map-module) requires a function that will be called to extend the supplied instance.

You can implement your own custom function by including a `pipeline.py` file in the same directory where the `pipeline.yml` file is located. Alira will automatically load this file and make every function in it available under the following namespace: `{pipeline name}.pipeline.{function name}`.

For example, look at the following `pipeline.py` file:

```python
def sample_function(instance: Instance) -> dict:
    return {
        "hello": "world"
    }
```

You can reference `sample_function()` from your `pipeline.yml` as follows:

```yaml
name: thermal

pipeline:
- module: alira.modules.Map
    function: thermal.pipeline.sample_function
```

This is the breakdown of the `function` attribute:

* `thermal`: The name of the pipeline.
* `pipeline`: This is an arbitrary section indicating that this code is part of the `pipeline.py` file.
* `sample_function`: The name of the function that will be called (this function should exist in the `pipeline.py` file.)

## Running the test suite

To run the test suite, you can follow the instructions below:

1. Create a `.env` file in the root of the project with your AWS credentials
2. Create and activate a virtual environment
3. Install the requirements from the `requirements.txt` file
4. Run the tests using `pytest`.

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pytest -s
```

Here is an example of the `.env` file:

```
AWS_ACCESS_KEY_ID=<your access key>
AWS_SECRET_ACCESS_KEY=<your secret key>
AWS_REGION_NAME=<your region>
```

To run the AWS integration tests:

```shell
$ pytest -s -m aws
```
