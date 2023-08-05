# alira

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
