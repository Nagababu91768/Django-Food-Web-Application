# Django-Food-Web-Application
This project intention to discover major concepts in Django to create a Food ordering items reusable webapp through online and offline also user submit their ideas then we collaborate with them.

## features
   - This project provides Authentication and Autharization along with permissions
   - Add food items to cart
   - Remove items from cart
   - submit ideas on web and check the status of the ideas
   - to use our code with other project webapps also
   - developed functional testing (automation testing using selenium)  and unittesting functionalities
  
## Installation
Use the package manager [pip](https://pypi.org/project/Nagababu-Django-Webapps/) to install Food Apps.

   ![reusable-Nagababu--Django--Webapps-brightgreen](https://user-images.githubusercontent.com/92179722/136641277-4bff24db-8a7e-442a-af2a-ca1dd560d94a.png) ![pypi-v0 0 (2)](https://user-images.githubusercontent.com/92179722/136641282-420aa7fa-6b51-4748-8eba-0665e25ea913.png) ![status-stable-yellowgreen](https://user-images.githubusercontent.com/92179722/136641387-37f4a2d3-a73c-4de0-8c14-351bafd909b5.png)

```bash
pip install Nagababu-Django-Webapps
```
## Usage  (This is a resuable package using web functionalities in other projects along with custom apps )
- Install Package Use the package manager [pip](https://pypi.org/project/Nagababu-Django-Webapps/)

   ![install](https://user-images.githubusercontent.com/92179722/136639763-0ef05376-df86-4b0c-91ee-24ff6f6e1e95.png)

- Create django Project

   ![git1](https://user-images.githubusercontent.com/92179722/136639707-144c7237-b6a6-4a36-a3d5-b40777655299.png)
   
 - Add "webapp1,webapp2,webapp3 , widget_tweaks,crispy_forms," to your INSTALLED_APPS setting like this

   ![git2](https://user-images.githubusercontent.com/92179722/136639324-92f108a4-995a-4837-8c41-7d52291c7441.png)
  
- Configure webapp1,webapp2,webapp3 in urls.py
      
   ![git3](https://user-images.githubusercontent.com/92179722/136639415-3afea528-ff8e-48ea-8b98-0808d8618d8e.png)
   
- Create a email_info.py and configure the email
   ![git13](https://user-images.githubusercontent.com/92179722/136639932-2bb98565-8e16-472d-900e-0d5cb030a77c.jpg)

- In settings.py include email_info.py 

   ![git20](https://user-images.githubusercontent.com/92179722/136639980-b129aff2-086d-4008-89c6-b74b6b4c5832.jpg)
   
- Enable Less secure allow access in email account

   ![git23](https://user-images.githubusercontent.com/92179722/136639996-aaa73733-faa0-4792-a324-71052a674f86.png)
- Apply migration on project and apply those migration on Database use makemigrations and migrate using command line utility called "manage.py"

   ![git4](https://user-images.githubusercontent.com/92179722/136640084-97d0ec38-68c0-4aef-81a8-a750b2406f55.png)
 
- To access Database or Admin create a Superuser visit   http://127.0.0.1:8000/admin/

   ![git7](https://user-images.githubusercontent.com/92179722/136640102-257365fa-6f11-407d-aa6c-858223f289f3.png)

- Runser server using manage.py , once done click on generated server user http://127.0.0.1:8000/
  
   ![git5](https://user-images.githubusercontent.com/92179722/136640119-677965af-3322-4e7f-8dae-f9c6c4f27c08.png)
   
- Navigated to Home page 

   ![git6](https://user-images.githubusercontent.com/92179722/136640158-23bb3d9e-6a31-4d3a-9adb-6ce4648bda9e.png)
   
- for registration click in Registration link on homepage

   ![regi](https://user-images.githubusercontent.com/92179722/136640172-50a2032c-6fd5-45a0-a7e4-a2bbd32a0110.png)

- for login click in Login link on homepage , once you logged have a access to add items to cart

   ![login](https://user-images.githubusercontent.com/92179722/136640180-e699acf9-8c20-4fd9-ab1f-d710c8042dc7.png)

- Menu item
 
   ![items](https://user-images.githubusercontent.com/92179722/136640198-77d6225e-fc46-4a4d-8f3c-51b0db205316.png)

- items page

   ![order_items](https://user-images.githubusercontent.com/92179722/136640219-6c87f0e9-aa8f-4bb1-b315-1b9de02e7ea1.png)
   
- Reusable Project file

   [Test.zip](https://github.com/Nagababu91768/Django-Food-Web-Application/files/7314868/Test.zip)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

