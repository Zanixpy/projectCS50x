async function getAPI(url)
{
  try
  {
    const response = await fetch(url,
        {
            method: "GET",
        });
    if (!response.ok)
        throw new Error(`Response status: ${response.status}`)
    const result = await response.json()
    return result
  } catch (error){
    console.error(error.message)
    return
  }
}

function handleElem(tab, elem, name)
{
    for (let i = 0; i < tab.length; i++) {
        if (tab[i].classList.toggle(name) && tab[i] != elem)
            tab[i].classList.remove(name)
        elem.classList.add(name)
    }
}

function getClickHandler(getA, elem) {
    return function() {
        handleElem(getA, elem, "click")
    }
}

function endEventInputs()
{
    let getQ = document.querySelectorAll('.question')
    for (let i = 0; i < getQ.length; i++) {
        let getA = document.querySelectorAll('.inputs-' + getQ[i].getAttribute("name"))
        getA.forEach(elem => {
            if (elem._clickHandler) {
                elem.removeEventListener("click", elem._clickHandler);
                delete elem._clickHandler;
            }
        })
    }
}

function eventInputs()
{
    let getQ = document.querySelectorAll('.question')
    for (let i = 0; i < getQ.length; i++) {
        let getA = document.querySelectorAll('.inputs-' + getQ[i].getAttribute("name"))
        getA.forEach(elem => {
            const handler = getClickHandler(getA, elem);
            elem._clickHandler = handler;
            elem.addEventListener("click", handler);
        })
    }
}

function editTemplate(question, answers)
{
    let clon = document.querySelector('.struct').content.cloneNode(true)

    clon.querySelector('.question').innerText = question['question']
    clon.querySelector('.question').setAttribute("name", question['id'])

    let getinput = clon.querySelectorAll('.ans')

    for (let j = 0; j < getinput.length; j++) {
        getinput[j].setAttribute("value", answers[j]['ans'])
        getinput[j].setAttribute("name", "ans-" + answers[j]['id'])
        getinput[j].classList.add(answers[j]['loc'])
    }

    document.querySelector('button').before(clon)
}

function createTemplates(dataQ, dataA)
{
    for (let i = 0; i < dataQ.length; i++) {
        let ans = []
        for (let k = 0; k < dataA.length; k++) {
            if (dataQ[i]['id'] == dataA[k]['question_id'])
                ans.push({'ans':dataA[k]['answer'], 'id':dataA[k]['ans_id'], 'loc':"inputs-" + dataQ[i]['id']})
        }
        editTemplate(dataQ[i], ans)
    }
}

function sendAnswers()
{
    document.querySelector("form").addEventListener("submit", (e) => {
        e.preventDefault()
        endEventInputs()
        document.querySelector(".btn").disabled = true
        console.log(document.querySelector(".btn"))
        let getA = document.querySelectorAll(".click")
        console.log(getA)
    }, {passive:false})

}

async function quiz(page) {
    const questions = await getAPI("/api/" + page + "/questions")
    const answers = await getAPI("/api/" + page + "/answers")
    createTemplates(questions,answers)
    eventInputs()
    sendAnswers()


}

document.addEventListener("DOMContentLoaded", () => {
    const page = document.body.dataset.page
    if (page == "anime")
        quiz("anime")
    else if (page == "manhwa")
        quiz("manhwa")
})
