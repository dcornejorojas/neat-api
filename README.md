## Neat's Pokemon adoption API

## Intro
**READ ALL THE DOCUMENT BEFORE YOU START TO CODE**
In this exercise you have to build an API exposed to the world that allows Neat to have Pokemon's adoption center. For a deeper DX you can hear [this](https://www.youtube.com/watch?v=3Q0nQQIKESw)
Every task that has the **(EXTRA)** tag means that we are thinking on implementing but **it is not necessary** for the MVP.
## What is the problem?
In Neat's adoption center, we always have around 3-6 pokemons (it can be more than 1 of the same pokemon) that are not adopted every day. We analized our data and did a market research, both suggest that we should create an API that allows more people to adopt these pokemons then everyone finds a home. If a pokemon is not adopted we must to send them to the team rocket's care facility (more like careless).
## How does the adoption center work?
### Adoption request
Every time we receive an adoption request, a new trainer need to submit a form (JSON body) with the following information.
1. Name
2. Lastname
3. Address
4. RUT
5. Small description on why we should give it to you
6. (EXTRA) An attachment with extra documentation
Each request can be accepted or denied, normally our acceptance rate is about 50%.
(EXTRA) If a person (identified by rut) had adopted a pokemon with us before, the acceptance rate is increased to 95%.
### Adoption deliver
When an adoption is accepted we have the following process:
1. Preparation: This step takes about 60 seconds and is a standard mandatory procedure for every association. We need to store all information of the request and the adopted pokemon for possible audit or future records.
2. (EXTRA)Transportation: This process take between 1-3 minutes (yes, we are the fastest in the area thanks to our Doduo's delivery system). This process some times failed (around 5%) due to a wrong address. Normally we just unify this process with the preparation but a recent research showed that people is so anxious waiting because they want to know more details about the process. 
3. Success: This is a final step for a happy story.
4. (EXTRA) Failure: Means that we could not deliver the pokemon and the adoption process is dropped. This require to undo all previuos steps
*We are very tidy and we try to store all data if something happen on the process (one time there was a Snorlax on the road and thanks to our detailed log we appeared on local news)

### Pokemon Handling (EXTRA)
Some times pokemons get sick and we have to send them to nurse Joy. The transportation takes around 1 hr and she takes between 4 hr to 5 days to heal them and send them back.

## What do we expect?
### Bussiness
An API where **anyone** can know all pokemons that are still un-adopted, our users are very visual so we think that a basic HTML response with information and a photo of each pokemon is needed. We want to set **some security rules** (we are not experts but we know that hacking is growing these days) on the adoption request, we are happy to use your recommended security method, but please have in mind that normally trainers are in a hurry so it cannot be so complex. For last, we want that everyone that have an accepted adoption request **can know their adoption status when they want**, we always assign a unique identification number for each adoption.
(EXTRA) We were thinking that if someone has 5 retries on a row we should block them for 1 day to avoid spam (on the request form submittion).
(EXTRA) If somebody is blocked more than 3 times we should send an email to officer Jenny (jenny@neatpagos.com) and to inform suspicious activity.

### Technical
We expect you to build this on a new Firebase project (they have a generous free tier), emulating all our waiting process and building the core the API. Here you will have to design the arhitecture of the back-end and which GCP products should we use. Also you have to use the [Pokemon API]([https://pokeapi.co/) and to validate that the pokemons are real and get useful information about pokemons like, name, type, photo and learned abilities.
### General
We trust your judment on all other details that are not specified, but please think about our business/customers when you build it, we are very customer centric.
Have in consideration that our friend, Professor Elm, will evaluate your API, so you have to **deliver your Repository and Firebase project** (owner access) to him and **to notify it via email to elm@neatpagos.com**. He will look for **prioritization**, **code quality** and **functionality**.
You have one week to finish the task and we expect that you do **not invest more than 13 hours** in this project
