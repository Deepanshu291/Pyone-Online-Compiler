
setTimeout(loading,1500 );



function loading() {
    var loader = document.getElementById('loading');
    loader.style.display = "none";

    window.addEventListener("load",  ()=>{
    
    loader.style.display = "none"
});
}


function submitform(){
    document.getElementById('code').submit()
}

function update(text) {
    let result_element = document.querySelector("#highlighting-content");
    // Update code
    result_element.innerText = text;
    // Syntax Highlight
    Prism.highlightElement(result_element);
  }