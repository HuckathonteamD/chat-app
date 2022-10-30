const updateChannelBtn = document.getElementById("update-channel-btn");
const updateChannelModal = document.getElementById("update-channel-modal");
const updatePageButtonClose = document.getElementById("update-page-close-btn");

const updateChannel = () => {
  if (uid !== channel.uid) {
    return;
  } else {
    updateChannelModal.style.display = "block";
  }
};
updateChannelBtn.addEventListener("click", updateChannel);

updatePageButtonClose.addEventListener("click", () => {
  updateChannelModal.style.display = "none"});

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", (e) => {
  if (e.target == updateChannelModal) 
    updateChannelModal.style.display = "none";
});
