let searchText = document.querySelector('input[type=text]')
let searchButton = document.querySelector('input[type=submit]')
let deleteButton = document.querySelector("input[name=delete]")
let deletePost = document.querySelector('input[name=post_id]')
let wrapper = document.querySelector('wrapper')
let searchUrl = "http://127.0.0.1:5555/search?search_text="
let deleteUrl = "http://127.0.0.1:5555/delete?post_id="

async function createTable(parent, data) {
    let table = document.createElement('table')
    let header = table.insertRow(0)
    header.style.fontWeight = '900'
    let ID = header.insertCell().innerText = "ID"
    let Rubrics = header.insertCell().innerText = "Rubrics"
    let Text = header.insertCell().innerText = "Text"
    let CreatedDate = header.insertCell().innerText = "Created Date"
    for (let post in data.reverse()) {
        let row = table.insertRow(1)
        let ID = row.insertCell(0).innerHTML = data[post]["id"]
        let Rubrics = row.insertCell(1).innerHTML = data[post]["rubrics"]
        let Text = row.insertCell(2).innerHTML = data[post]["text"]
        let CreatedDate = row.insertCell(3).innerHTML = new Date(data[post]["created_date"]).toDateString()
    }
    parent.replaceWith(table)
}


searchButton.addEventListener("click", async function (event) {
    event.preventDefault()
    let rawPosts = await fetch(searchUrl + searchText.value)
    let jsonPosts = await rawPosts.json()
    await createTable(wrapper, jsonPosts)
})

deleteButton.addEventListener('click', async function (event) {
    event.preventDefault()
    let deletedPost = await fetch(deleteUrl + deletePost.value)
    let responseOfDelete = await deletedPost.json()
    console.log(responseOfDelete["detail"])

    if (responseOfDelete["detail"] === "Not Found") {
        wrapper.innerHTML = responseOfDelete["detail"]
    } else wrapper.innerHTML = `Deleted post with ID = ${deletePost.value}`


})

