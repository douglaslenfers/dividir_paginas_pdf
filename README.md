## Splitting pdf pages

### Prerequisites


```
Python 2.7.6
Django 1.9.0
PyPDF2 1.2.6
```

### Installing

Run the command:

```
git clone https://github.com/douglaslenfers/split_pdf_python.git
```

And everything will be setup.

## Built With

* [Python] 2.7.6 (https://www.python.org/download/releases/2.7.6/) - The programming language
* [Django] 1.9.0 (https://docs.djangoproject.com/en/2.1/releases/1.9/) - The web framework
* [PyPDF2] 1.2.6 (https://pythonhosted.org/PyPDF2/) - The pdf manager

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run Django

    $ python manage.py runserver $IP:$PORT

## Splitting the Pdfs.

After running the server you can ping to simply verify if it's running ok.
> https://yourserver.com/

> repsonse:
```
{
    "ping": "pong"
}
```

To split pdfs you can post, passing through the absolute input_path and the absolute output_path:
> https://youserver.com/

> request:
```
{
  "input_path" : "/home/ubuntu/workspace/split_pdf/original/file.pdf",
  "output_path" : "/home/ubuntu/workspace/split_pdf/splitted/"
}
```
> response:
```
{
  "total_pages": total of pages that has been splitten
  "input_path" : "/home/ubuntu/workspace/split_pdf/original/file.pdf",
  "output_path" : "/home/ubuntu/workspace/split_pdf/splitted/file_name/"
}
```

## Authors

* **Douglas Lenfers** - [Douglas Lenfers](https://github.com/douglaslenfers)
* **Matheus dos Santos** - [Matheussf](https://github.com/matheussf)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

