
function pagination(id) {
    let href = ''

    let et = document.getElementById('Et')
    let pr = document.getElementById('Pr')
    let ua = document.getElementById('Ua')
    let lt = document.getElementById('LT')
    let pc = document.getElementById('PC')
    let all_et = document.getElementById('all_et')
    let all_cat = document.getElementById('all_cat')


    if (et.checked) { href += 'estado=Et&' }
    if (pr.checked) { href += 'estado=Pr&' }
    if (ua.checked) { href += 'estado=Ua&' }
    if (lt.checked) { href += 'categoria=LT&' }
    if (pc.checked) { href += 'categoria=PC&' }
    if (all_cat.checked) { href += 'categoria=all&' }
    if (all_et.checked) { href += 'estado=all&' }


    aLink = document.getElementById(id)
    ahref = aLink.getAttribute('href')
    aLink.setAttribute('href', `${ahref}&${href}`)
}