
// getSelectValue();


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