function display() {
    let temp = document.querySelector('.struct')
    let clon = temp.content.cloneNode(true)
    clon.querySelector('.question').content = "Who's mc in Naruto ?"

    let listans = ["Naruto","Sasuke","Sakura"]
    let getinput = clon.querySelectorAll('.ans')
    console.log(getinput)

    for (let i = 0; i < listans.length; i++) {
        getinput[i].innerText = listans[i]   
    }

    document.body.append(clon)
}

display()
/*function Affichage(x) {
    const temp= document.querySelector('.struct')
    const clone= temp.content.cloneNode(true)
    clone.querySelector('.question').innerText=x[window.val].question

    clone.querySelector('.ans.first').innerText= x[window.val].reponse[0].ans
    clone.querySelector('.ans.first').setAttribute("data-verifans",x[window.val].reponse[0].trueans)

    clone.querySelector('.ans.second').innerText= x[window.val].reponse[1].ans
    clone.querySelector('.ans.second').setAttribute("data-verifans",x[window.val].reponse[1].trueans)

    clone.querySelector('.ans.third').innerText= x[window.val].reponse[2].ans
    clone.querySelector('.ans.third').setAttribute("data-verifans",x[window.val].reponse[2].trueans)
    document.querySelector('.mainAct').append(clone)
}

function System(y) {
    document.querySelectorAll('.ans').forEach(element => {
        element.addEventListener('click', e =>{
            if (e.target.dataset.verifans==="true") {
                document.querySelector('.number').textContent++
                e.target.classList.add('winner')
            }else{
                e.target.classList.add('loser')
            }
            setTimeout(()=>{
                document.querySelector('.quiz').remove()
                window.val++

                if (window.val < y.length) {
                    Affichage(y)
                    System(y)
                }else{
                    FinQuiz()
                }
            },300)
        },{once:true})
    })
}

function FinQuiz() {
    const mainAct = document.querySelector('.mainAct')
    mainAct.innerHTML = "<h2>Quiz terminé !</h2><p>Score : " + document.querySelector('.number').textContent + "</p>"
}*/
