// チャンネルアップデート
const updateChannelBtn = document.getElementById("update-channel-btn");
const updateChannelModal = document.getElementById("update-channel-modal");
const updatePageButtonClose = document.getElementById("update-page-close-btn");

// チャンネルフォロー
const followChannelBtn = document.getElementById("follow-channel-btn");
const followChannelModal = document.getElementById("follow-channel-modal");
const followPageButtonClose = document.getElementById("follow-page-close-btn");

// モーダルを開く
function modalOpen(mode) {
  if (mode === "update") {
    if (uid !== channel.uid) {
      return;
    } else {
      updateChannelModal.style.display = "block";
  } else if (mode === "follow") {
    followChannelModal.style.display = "block";
  }
}

updateChannelBtn.addEventListener("click", () => {
  modalOpen("update");
});
followChannelBtn.addEventListener("click", () => {
  modalOpen("follow");
  const followConfirmBtnLink = document.getElementById("follow-confirm-link");
  const followUrl = `/follow/${channel.id}`;
  followConfirmBtnLink.setAttribute("href", followUrl);
});

// モーダルを閉じる
function modalClose(mode) {
  if (mode === "update") {
    updateChannelModal.style.display = "none";
  } else if (mode === "follow") {
    followChannelModal.style.display = "none";
  }
}

updatePageButtonClose.addEventListener("click", () => {
  modalClose("update");
});
followPageButtonClose.addEventListener("click", () => {
  modalClose("follow");
});

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", (e) => {
  if (e.target == updateChannelModal) {
    updateChannelModal.style.display = "none";
  } else if (e.target == followChannelModal) {
    followChannelModal.style.display = "none";
});
