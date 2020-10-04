# Assessment for Section 4
For the Section 4, the assessment is made by the following parts:

- Create a **Quote** model, with _author_, _quote_, _context_, _source_, _created_at_ as fields.
- Create the **1st endpoint**, in /api/quote, which provide a list of quote (with a pagination of size = 30), with the possibility to create a new one.
- Create the **2nd endpoint**, in /api/quote/<int:pk>/, which provide details of a single quote with the possibility to update or delete it. 
- Only an administrator can create, update or delete a quote. A simple or even an unauthenticated user can only see the paginated list of quotes. 