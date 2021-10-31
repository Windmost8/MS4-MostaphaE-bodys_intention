# MS4 - Mostapha El Ansary - Body's Intention

## **UX**
---
### **Project Goals**
*Body's Intention* is a fitness oriented site with the intentions
as the name suggests, to provide users with the platform to not
only have the ability to purchase for relevant products, but also inquire about them. 
Anyone who cares about their body will find this site caterd to 
their needs.

### **User Stories**

As an **aspiring** and **already** fitness oriented individual, I would want:

1. To easily be able to **purchase** products.
2. To be able to **inquire** about anything related to the products.
3. To have my own **profile** in which I interact with the site, such as being able to view profile histories, or the abiltiy to comment on products.

---

## **Typography & Color Scheme**
---
I opted to gith a predominantly black and white look (which also existed with boutique ado) as I thought the contrast workeed best with eachother, and any colors present in any images and products stand out even more becuase of it.

Buttons were stylized black and white to differnetiate them from eachother and represent what they do.

When it comes to CRUD buttons, then mostly they are red and blue as is what feels natural.

A mixure of lato and garamond were used for typograhy as is what I felt contrasted best with the color scheme. In general, titles and subtitles resembled eachother across pages so as to remain consistent. 

## **Wireframes**
---
All intial wireframes can be found in the "wireframes" folder directory
or alternatively accessed through the link below; 

https://github.com/Windmost8/MS4-MostaphaE-bodys_intention/blob/c5317364816c54fd880a52a4555d37d94b197a75/wireframes

Site differed slighly in the end with more profile pages, error pages, and other additional features that all built upon the intial wireframes (mobile and desktop), with tablet being similar.

---

## **Technology**
---
* HTML
* CSS
* Bootstrap 
* Python
* Chrome DevTools/Lighthouse Audits
* Github
* Gitpod 
* Django
* Heroku 
* Amazon Web Services (S3)
* Fontawesome
* Balsamiq
* allauth (https://django-allauth.readthedocs.io/en/latest/installation.html)
* additional technologies can be found in the requirements.txt file

## **Features**
---
### **Existing Features**

**Navigation** - There is an easy-to-navigate navigation menu for both desktop and mobile view, one "set" of menus for the site as a whole, and another for products. From the navigation menus you may reach all relevant pages. The products menu can filter based on category. Additionally, there is a search bar that will navigate you towards certain products if you search for it. On the products page, there is also a scroll up button present.

**Products** - This ecommerce site allows for the abiltiy to browse and purchase products. One may do so both anonymously, or as a logged in user with an account.
Browsing products you may sort them by price, name, category, or rating. Additionally clicking on a product will reveal it's product details, and the abiltiy to continue on with a purchase, or add them to a shopping bag as one may choose to continue browsing. Additionally, you may also use the search bar to find certain products, searching for either names of products or their categories.
 
**Account** - Users may choose to log in or create an account. Logged in users have access to their profile page, where order, comment, and contact summaries are listed, as well as their account information. Here they may (lining up with CRUD guidelines) edit or delete their past comments and inquiries (contacts). In additon, logged in users will have their name shown on public comments.  

**Comments** - Only logged in users may add a comment under products details. If there are none, then an option to go ahead is displayed. Adding comments will make them visible publicly to others who visit that specific product details page. The date it was submitted is also shown. For logged in users, they may navigate to their comment history page and edit and delete as they wish, as followed by the CRUD guidelines.

**Contact** - Both logged in and anonymous users may utilize the contact feature to send inquires on anything related to the site. Users are prompted to enter their name and also an email, alongside the inquiry itself. This inquiry may then later be viewed in logged in user's contact history, under their profile, as followed by the CRUD guidelines.

**Social Media** - There is a social media footer present in every page where any user may access. They open new tabs on relevant social media sites.

**Admin** - For admin users, there is further utility in the form of being able to add product, edit, or delete products, alongside also being able to edit/delete public comments found on the product detail pages.

**Checkout** - Once any user has decided to go along with payment, users are taken to the order page where they must fill in relevant information required for purchase. Upon succeful purchases and order summary is generated and an email sent to chosen email. If a user had added products to the shopping bag, but regret their choice, they may remove it entirely or edit their choice in the form of updated the quantity of a chosen product for purchase for example.

**About Us** - There is an about us page dedicated to anyone who would like to know more about the site and its features, as well as how to navigate it. 

### **Features Left to Implement**

**Pagination** - Pagination is a feature that may be implemented to the parts of the site that have the abiltiy to host multiple entries, such as products and comments.

**Further Comment Features** - A thumbs up or thumbs down feature or stars review feature are ones that may be implemented to further enhance the functionality of commenting, as well as the ability to reply to certain comments.

**Favorites/Like Button / Wishlist** - A favorites/like button, or a add to wishlist feature, which are similiar, are both features that may be implemented to increase engagement with the site as well as with profiles.

### **Screenshots**
All screenshots relevant to the features can be found in the screenshots folder directory.

---

## **Testing**
---
### **Validator Testing**

* HTML (https://validator.w3.org/) (through URI) (only 2 "warnings" that were both "The type attribute is unnecessary for JavaScript resources." Could not find.)

* CSS (https://jigsaw.w3.org/css-validator/)

* Javascript (https://jshint.com/)

* Python (http://pep8online.com/) & (Pylint)

* Lighthouse Chrome DevTools

### **Unfixed Bugs**
At times the account button navigation menu bugs out and you are unable to select an option unless you refresh.
There are also some pylint errors and other errors that remained, which came with django, and others that doesn't affect the projects functionality

### **Test Cases**
* Typing in a false url should reusult in an error page.
* It is also impossible to access existing urls if you as a user do not have access (for example as an admin, or anonymous user).
* All required fields must be filled before submitting
* All crud funtioncality correctly updates the database and page shown
* All social media links open a new tab.
* Actions requring a log in would prompt users who are not signed in to log in or sign up
* Emails sent to the user are sent successfully (not inquiries)
* Scroll button and sort filtering work as intended
* Search for category or name correctly shows the results
### **Supported Screens & Browsers**
* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold
* Google Chrome **(Browser)** Mostly
* Firefox **(Browser)**
* Microsoft Edge **(Browser)**
---

## **Deployment**
---
### **Gitpod**
Gitpod was used for source control alongside its commit history. 

In order to commit, whilst still in gitpod, running the command git add . (or a specific file/folder instead of "." (without the quotes)), will add all the changes you have done to be prepared for a commit.
After this step, you may run the command git commit -m "your comment" (your comment being whatever message you want to convey alongside the commit). Running this will show how much changes were done, through the terminal.
Finally, running the command git push should put your changes and project into your repository.
### **Heroku**
With heroku, it was possible to link your gitpod in order to deploy. In heroku there are config variables set.

Deployment on Heroku was done through their official website https://www.heroku.com/.
One must intially create an app name on Heroku, and then we connect that app to our github project respository.
For this project, automatic deployment was used from the Heroku site.
Once you have connceted your git repo with heroku, you should then access the settings and "reveal config vars". Here we can securely tell heroku which variables are required for deployment

Additionally, the requirements.txt file must be constantly updated if any new installs were used, so that heroku knows.

### **Amazon Web Services**
Amazon web serives S3 storage and buckets were used to host the static and media files of the deployed site. https://aws.amazon.com/

---

## **Credits**
Code institute is to be credited with providing help in implementing payment (and stripe), account creation (also alluth), product creation and display, certain CSS/JS, CRUD guidelines, and checkout and bag functionality.

---
### **Content**
### **Media**
Background image was found here;
https://www.freepik.com/free-photos-vectors/fitness-background

Product images were found here (free stock photos); https://www.pexels.com/