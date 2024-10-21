# Project Overview

This project includes the following changes and implementations:

## Updates to Templates

1. **`book_list.html`**:
   - Modifications were made to improve or update the existing content and structure.

2. **`success/contact_success.html`**:
   - Created a new template to display a success message after a user submits the contact form.

3. **`contact.html`**:
   - A new contact form template was created where users can input their name, email, and message.

## Forms

- A new file `forms.py` was created to handle form-related code.
- Implemented a **signup form** in `forms.py` for user registration, which was imported into the `views.py` file.

## Views

- A new class `ContactFormView` was created in `views.py` to handle the contact form logic.
  - This class renders the `contact.html` template and processes the form submissions.

## URLs

- Two new paths were added to `urls.py`:
  - **`contact/add/`**: Handles displaying the contact form and processing submissions.
  - **`contact/success/`**: Redirects to a success page after a form is successfully submitted.

## Features

- The project now supports:
  - Displaying a contact form on the `/contact/add/` page.
  - Showing a success message on the `/contact/success/` page after successful form submission.
