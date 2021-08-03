# PyCSS

## What is it?
PyCSS is a micro-framework to speed up the process of writing bulk CSS classes.   

## How does it do it?
With Python!!!  
First download the [https://github.com/Jammin-Coder/py-css/tree/main/PythonCSS](PythonCSS) folder that contains the program files, then in that directory open the `app.py` file:  
![app py](https://user-images.githubusercontent.com/73239367/127931505-b7f406b5-0938-4926-8906-04a73ef4b2b2.png)  


Then within `app.py` and within the `CSSClasses` class, you write Python classes that translate into CSS:  
![css](https://user-images.githubusercontent.com/73239367/128073098-9bc98671-3018-481c-ac07-7e455e475ef3.png)


Then you run `compile.py` with `python3 compile.py -o <output_css_file>.css`: 
The `-o` flag tells the program where to output the compiled CSS file.  
![Screenshot from 2021-08-02 18-36-47](https://user-images.githubusercontent.com/73239367/127932297-4800082d-3c30-42fe-9998-51ce044a0e74.png)  

Then open the css file and make sure it worked:  
![compiled_css](https://user-images.githubusercontent.com/73239367/128073710-ff8c509d-4f58-418e-8222-87f121a67050.png)


You can also inherit properties from other classes:  
![inheritence](https://user-images.githubusercontent.com/73239367/128074047-fceb8e22-2820-49b7-80f7-d6ed40d1c4e9.png)


which turns into this:  
![compiled_inheritence](https://user-images.githubusercontent.com/73239367/128074288-2cf67a63-0cfc-45c2-980e-ba00b31ccd75.png)



Then you can use the CSS file in any web-development project!


### More docs to come.
Feel free to ask in the discussions tab if you have any problems or questions.
