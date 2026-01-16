
document.addEventListener('mousemove', e => {
    Object.assign(document.documentElement, {
        style:`
        --x: ${(e.clientX - window.innerWidth / 2) * -.005}deg;
        --y: ${(e.clientY - window.innerHeight / 2) * -.01}deg;`
    })
})