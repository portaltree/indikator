# Indikator

Indikatoris a Python library for dealing with word pluralization.

## Installation

Use the `git clone` command in the directory for your project to install indikator.

```bash
git clone https://github.com/asimo10/indikator.git
```

## Quick Example

```python
import indikator as ik

total = 10 # The amount you want the progress bar to go
sum = 0

for count in range(total):
    # Put the code that you want to run while the progress bar is running inside here:
    sum += 1

    ik.bar(total, count, cnt)
    cnt += 1
    if cnt == 16:
        cnt = 0

print(sum)

# Returns 10
```

## IMPORTANT

You must always have at least the:

* `total`, `count`, and `cnt` parameter
* Always add the code that you want to run while running a progress bar in this format below

```python
import indikator as ik
for count in range(total):
    
    # YOUR CODE HERE
    
    ik.bar(total, count, cnt)
    cnt += 1
    if cnt == 16:
        cnt = 0
```



## Each parameter

There are 6 total parameters that you can add into bar function.

* [total](#total)
* [count & cnt](#count--cnt)
* [title](#title)
* [done_text & togo_text](#done_text--togo_text)

### total

The `total` parameter is to keep count of the number of calls. If the total is 100 it will take 100 calls to the bar function to complete.

### count & cnt

The `count` and `cnt` parameter is to keep track of how many times the progress bar had went and calculate all the stuff. The `cnt` parameter is different from the `count` parameter and is needed to be reset every 16 time.

### title

The `title` parameter is for the title used in the progress bar. If you don't add it, it will default to "Downloading".

### done_text & togo_text

The `done_text` and `togo_text` parameter is to set the text to be used in the progress bar. The default parameter is "#" and " ".

```
✓ Downloading: [####################] 10/10
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
