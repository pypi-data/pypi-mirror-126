# pollencli-pyline-removal

<p align="center">
  <a href="https://github.com/psf/black">
    <img
      alt="Issues"
      src="https://img.shields.io/badge/code%20style-black-000000.svg"
    />
</p>

## How to use

`rm-pyline <name_id> <src_filepath>` command

```bash
rm-pyline
```

### example

input python file : `input.py`

```py
def main():
    x: int = 1
    print(f"Hello, World! : {x}")


if __name__ == "__main__":
    main()

```

```sh
rm-pyline print ./input.py > output.py
```

`output.py`

- not formatted file
- There is no guarantee that the output is valid python code even if the input is.

```py
def main():
    x: int = 1
if __name__ == '__main__':
    main()
```
