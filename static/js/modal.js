// モーダルを表示させる

const addChannelModal = document.getElementById("add-channel-modal");
const deleteChannelModal = document.getElementById("delete-channel-modal");

const addPageButtonClose = document.getElementById("add-page-close-btn");
const deletePageButtonClose = document.getElementById("delete-page-close-btn");

const addChannelBtn = document.getElementById("add-channel-btn");

// const followChannelBtn = document.getElementsByClassName("follow-channel-btn-i");
const followChannelModal = document.getElementById("follow-channel-modal-i");
const followPageButtonClose = document.getElementById("follow-page-close-btn-i");

const unfollowChannelModal = document.getElementById("unfollow-channel-modal-i");
const unfollowPageButtonClose = document.getElementById("unfollow-page-close-btn-i");


// モーダルを開く
// <button id="add-channel-btn">新規チャンネル作成</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", () => {
  modalOpen("add");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "follow_i") {
    followChannelModal.style.display = "block";
  } else if (mode === "unfollow_i") {
    unfollowChannelModal.style.display = "block";
  }
}

// モーダル内のバツ印がクリックされた時
addPageButtonClose.addEventListener("click", () => {
  modalClose("add");
});
deletePageButtonClose.addEventListener("click", () => {
  modalClose("delete");
});
followPageButtonClose.addEventListener("click", () => {
  modalClose("follow_i");
});
unfollowPageButtonClose.addEventListener("click", () => {
  modalClose("unfollow_i");
});

function modalClose(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "none";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "follow_i") {
    followChannelModal.style.display = "none";
  } else if (mode === "unfollow_i") {
    unfollowChannelModal.style.display = "none";
  }
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  } else if (e.target == deleteChannelModal) {
    deleteChannelModal.style.display = "none";
  }
}