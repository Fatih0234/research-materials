[ Jump to content ](https://create.t3.gg/en/introduction#content)
[ ![T3 Logo Dark](https://create.t3.gg/images/t3-dark.svg) ![T3 Logo Light](https://create.t3.gg/images/t3-light.svg) ](https://create.t3.gg/ "Home")
[ Docs ](https://create.t3.gg/en/introduction)[ FAQ ](https://create.t3.gg/en/faq)
[ GitHub ](https://github.com/t3-oss/create-t3-app)
Toggle sidebar
Search
Press `/` to search
Search
Press `/` to search
  * ##  Create T3 App 
    * [ Introduction ](https://create.t3.gg/en/introduction)
    * [ Why CT3A? ](https://create.t3.gg/en/why)
    * [ Installation ](https://create.t3.gg/en/installation)
    * [ Folder Structure (Pages) ](https://create.t3.gg/en/folder-structure-pages)
    * [ Folder Structure (App) ](https://create.t3.gg/en/folder-structure-app)
    * [ FAQ ](https://create.t3.gg/en/faq)
    * [ T3 Collection ](https://create.t3.gg/en/t3-collection)
    * [ Examples ](https://create.t3.gg/en/examples)
    * [ Other Recommendations ](https://create.t3.gg/en/other-recs)
  * ##  Usage 
    * [ First Steps ](https://create.t3.gg/en/usage/first-steps)
    * [ Next.js ](https://create.t3.gg/en/usage/next-js)
    * [ TypeScript ](https://create.t3.gg/en/usage/typescript)
    * [ tRPC ](https://create.t3.gg/en/usage/trpc)
    * [ Drizzle ](https://create.t3.gg/en/usage/drizzle)
    * [ Prisma ](https://create.t3.gg/en/usage/prisma)
    * [ NextAuth.js ](https://create.t3.gg/en/usage/next-auth)
    * [ Environment Variables ](https://create.t3.gg/en/usage/env-variables)
    * [ Tailwind CSS ](https://create.t3.gg/en/usage/tailwind)
  * ##  Deployment 
    * [ Vercel ](https://create.t3.gg/en/deployment/vercel)
    * [ Netlify ](https://create.t3.gg/en/deployment/netlify)
    * [ Docker ](https://create.t3.gg/en/deployment/docker)


[](https://create.t3.gg/)
[Introduction](https://create.t3.gg/en/introduction)
On this page
#  [ Introduction ](https://create.t3.gg/en/introduction#overview)
App Router Pages Router
## [The T3 Stack](https://create.t3.gg/en/introduction#the-t3-stack)
The _“T3 Stack”_ is a web development stack made by [Theo↗](https://twitter.com/t3dotgg) focused on simplicity, modularity, and full-stack typesafety.
The core pieces are [**Next.js** ↗](https://nextjs.org/) and [**TypeScript** ↗](https://typescriptlang.org/). [**Tailwind CSS** ↗](https://tailwindcss.com/) is almost always included. If you’re doing anything resembling backend, [**tRPC** ↗](https://trpc.io/), [**Prisma** ↗](https://prisma.io/), and [**NextAuth.js** ↗](https://next-auth.js.org/) are great additions too.
You may have noticed that there are a… lot of pieces. That’s by design. Swap pieces in and out as you need - this stack is modular at its core :)
## [So… what is create-t3-app? A template?](https://create.t3.gg/en/introduction#so-what-is-create-t3-app-a-template)
Kind of? 
`create-t3-app`
is a CLI built by seasoned T3 Stack devs to streamline the setup of a modular T3 Stack app. This means each piece is optional, and the “template” is generated based on your specific needs. 
After countless projects and many years on this tech, we have lots of opinions and insights. We’ve done our best to encode them into this CLI.
This is **NOT** an all-inclusive template. We **expect** you to bring your own libraries that solve the needs of **YOUR** application. While we don’t want to prescribe solutions to more specific problems like state management and deployment, we [do have some recommendations listed here](https://create.t3.gg/en/other-recs).
## [T3 Axioms](https://create.t3.gg/en/introduction#t3-axioms)
We’ll be frank - this is an _opinionated project_. We share a handful of core beliefs around building and we treat them as the basis for our decisions.
### [Solve Problems](https://create.t3.gg/en/introduction#solve-problems)
It’s easy to fall into the trap of “adding everything” - we explicitly don’t want to do that. Everything added to 
`create-t3-app`
should solve a specific problem that exists within the core technologies included. This means we won’t add things like state libraries (
`zustand`
, 
`redux`
) but we will add things like NextAuth.js and integrate Prisma and tRPC for you. 
### [Bleed Responsibly](https://create.t3.gg/en/introduction#bleed-responsibly)
We love our bleeding edge tech. The amount of speed and, honestly, fun that comes out of new shit is really cool. We think it’s important to bleed responsibly, using riskier tech in the less risky parts. This means we wouldn’t ⛔️ bet on risky new database tech (SQL is great!). But we happily ✅ bet on tRPC since it’s just functions that are trivial to move off.
### [Typesafety Isn’t Optional](https://create.t3.gg/en/introduction#typesafety-isnt-optional)
The stated goal of Create T3 App is to provide the quickest way to start a new full-stack, **typesafe** web application. We take typesafety seriously in these parts as it improves our productivity and helps us ship fewer bugs. Any decision that compromises the typesafe nature of Create T3 App is a decision that should be made in a different project.
[ Why CT3A?](https://create.t3.gg/en/why)
* * *
##  More 
  * [ Edit this page ](https://github.com/t3-oss/create-t3-app/tree/main/www/src/pages/en/introduction.md)
  * [ Translate this page ](https://github.com/t3-oss/create-t3-app/blob/main/www/TRANSLATIONS.md)
  * [ Join Our Discord Community ](https://t3.gg/discord)


Recent Contributors To This Page [ Contributors ](https://github.com/t3-oss/create-t3-app/commits/main/www/src/pages/en/introduction.md)
[ ![Powered by Vercel](https://create.t3.gg/images/powered-by-vercel.svg) ](https://vercel.com/?utm_source=t3-oss&utm_campaign=oss)
##  On this page 
  * [ Introduction ](https://create.t3.gg/en/introduction#overview)
  * [ The T3 Stack ](https://create.t3.gg/en/introduction#the-t3-stack)
  * [ So… what is create-t3-app? A template? ](https://create.t3.gg/en/introduction#so-what-is-create-t3-app-a-template)
  * [ T3 Axioms ](https://create.t3.gg/en/introduction#t3-axioms)
  * [ Solve Problems ](https://create.t3.gg/en/introduction#solve-problems)
  * [ Bleed Responsibly ](https://create.t3.gg/en/introduction#bleed-responsibly)
  * [ Typesafety Isn’t Optional ](https://create.t3.gg/en/introduction#typesafety-isnt-optional)


##  More 
  * [ Edit this page ](https://github.com/t3-oss/create-t3-app/tree/main/www/src/pages/en/introduction.md)
  * [ Translate this page ](https://github.com/t3-oss/create-t3-app/blob/main/www/TRANSLATIONS.md)
  * [ Join Our Discord Community ](https://t3.gg/discord)


