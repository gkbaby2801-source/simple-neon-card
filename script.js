const btn = document.getElementById('glowBtn');
const avatar = document.querySelector('.avatar');
let followed = false;

btn.addEventListener('click', () => {
  followed = !followed;
  btn.classList.toggle('active', followed);
  btn.textContent = followed ? 'Following' : 'Follow';
  // small avatar pulse
  avatar.style.transform = followed ? 'scale(1.06)' : 'scale(1)';
  setTimeout(()=> avatar.style.transform = 'scale(1)', 400);
});
