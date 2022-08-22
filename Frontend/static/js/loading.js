
setTimeout(loading,1500 );



function loading() {
    var loader = document.getElementById('loading');
    loader.style.display = "none";

    window.addEventListener("load",  ()=>{
    
    loader.style.display = "none"
});
}