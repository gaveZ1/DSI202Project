$('.nav ul li').click(function() {

    $(this).addClass("active").siblings().removeClass('active')
})

const tapBtn = document.querySelectorAll('.nav ul li');
const tap =document.querySelectorAll('.profile-address-tap,.profile-orderhis-tap');
function taps(panelIndex) {
    tap.forEach(function(node) {
        node.style.display = 'none';
    });
    tap[panelIndex].style.display = 'block';
}
taps(0)
