# Semantic HTML tags
Here is a cheat sheet for modern, semantic HTML tags that define the structure and context of your web page content.
## Page Structure Tags
These tags define the main regions of your page layout.
```html
 <html>
   <body>
    <header>
        <nav>...</nav>
    </header>
    <main>
       <article>
           <section>...</section>
           <section>...</section>
       </article>
    </main>
    <aside>...</aside>
    <footer>...</footer>
   </body>
   </html>
```
`<main>` 
   * What it is: The main, unique content of the page.
   * Use: Wraps the primary topic of the page (e.g., the blog post, the product listing, the main part of the web app).
   * Rule: You should only have one `<main>` tag per page.
`<header>`
   * What it is: A container for introductory content or navigation links.
   * Use: Can be used for the entire site's header (logo, main menu, search bar) or for the header of a smaller section, like an `<article>`.
`<footer>`
   * What it is: A container for footer content.
   * Use: Typically found at the bottom of the page (or an `<article>`) and contains copyright info, related links, or author information.
`<nav>`
   * What it in is: A container for major navigation links.
   * Use: Wraps your main menu, breadcrumbs, or a table of contents. Don't use it for every group of links (e.g., footer links already inside a `<footer>` don't always need it).
`<aside>`
   * What it is: For content that is "tangentially related" to the main content.
   * Use: The perfect tag for a sidebar, call-out box, or a section for ads. If you removed it, the main content should still make sense.
## Content Grouping Tags
These tags group your content by its meaning and relationship.
 * <article>

   * What it is: A self-contained, independent piece of content.

   * Use: The best tag for a blog post, forum post, news article, or a product card. Ask yourself: "Could this piece of content stand on its own and still make sense?" If yes, use <article>.

 * <section>

   * What it is: A thematic grouping of content.

   * Use: Wraps a specific part of a page, like a "Contact Us" section, a chapter of an article, or a "Features" block on a homepage. It's more generic than <article>.

   * Rule: A <section> should almost always have a heading tag (like <h2>) inside it.

Text-Level & Media Tags

These tags give specific meaning to text or embed media.

 * <figure> & <figcaption>

   * What they are: A way to group media (like an image or code block) with a caption.

   * Use: Wrap the <figure> tag around your <img>, <video>, or <code> block. Then, place a <figcaption> tag inside it (as the first or last element) to provide a caption.

   <!-- end list -->

   <figure>

  <img src="chart.png" alt="Sales chart">

  <figcaption>Fig. 1: Sales growth over the last quarter.</figcaption>

</figure>

  

 * <time>

   * What it is: Marks a specific time or date.

   * Use: Wraps around a human-readable date. You can add a datetime attribute to give search engines and screen readers the precise, machine-readable date.

   <!-- end list -->

   Published on <time datetime="2025-11-08">November 8, 2025</time>

  

 * <mark>

   * What it is: Marks text as "highlighted" for reference.

   * Use: This is for highlighting text in a quote or bringing attention to text, like in search results. It's not for decoration.

 * <details> & <summary>

   * What they are: A "disclosure" widget that the user can open and close.

   * Use: The <summary> tag holds the always-visible title (e.g., "FAQ Question"). The rest of the content inside <details> is hidden until the user clicks it.

   <!-- end list -->

   <details>

  <summary>What is semantic HTML?</summary>

  <p>It's HTML that gives meaning to the content...</p>

</details>