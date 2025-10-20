# test_task
## Python junior test task

## Usage:

run in console:

```python
cd /to_script_folder

python main.py --files test/products1.csv test/products2.csv --report average rating
```


run example:

<img width="1020" height="135" alt="изображение" src="https://github.com/user-attachments/assets/e9582c46-ede9-4d05-bcdd-13a2e04be42b" />

## Tests:

run in console:

```python
pytest
```
<img width="1542" height="170" alt="изображение" src="https://github.com/user-attachments/assets/379a8f20-9299-47e3-aec6-2828a1e462d2" />


    


```python
pytest --cov=main --cov-report=html
```
then open /htmlcov/index.html in any browser

<img width="565" height="229" alt="изображение" src="https://github.com/user-attachments/assets/b36bbe42-a297-477e-834a-9f622a5f3ef1" />

