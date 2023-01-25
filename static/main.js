"use strict";
const form = document.querySelector('body > main > form')
const username = document.querySelector("body > main > form > input[name='username']")
const email = document.querySelector("body > main > form > input[name='email']")
const password = document.querySelector("body > main > form > input[name='password']")

form.onsubmit = async () => {
    event.preventDefault()

    const response = await fetch("/", {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify({
            "username": username.value,
            "email": email.value,
            "password": password.value
        })
    })
    const data = await response.json()
    console.log(data);
}