// モーダルを表示させる

const addChannelBtn = document.getElementById("add-channel-btn");
const addChannelModal = document.getElementById("add-channel-modal");
const addPageButtonClose = document.getElementById("add-page-close-btn");

const deleteChannelModal = document.getElementById("delete-channel-modal");
const deletePageButtonClose = document.getElementById("delete-page-close-btn");

const logoutBtn = document.getElementById("logout-btn");
const logoutModal = document.getElementById("logout-modal");
const logoutPageButtonClose = document.getElementById("logout-page-close-btn");

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
logoutBtn.addEventListener("click", () => {
  modalOpen("logout");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "logout") {
    logoutModal.style.display = "block";
  } else if (mode === "follow_i") {
    followChannelModal.style.display = "block";
  } else if (mode === "unfollow_i") {
    unfollowChannelModal.style.display = "block";
  }
}

// モーダル内のキャンセルがクリックされた時
addPageButtonClose.addEventListener("click", () => {
  modalClose("add");
});
deletePageButtonClose.addEventListener("click", () => {
  modalClose("delete");
});
logoutPageButtonClose.addEventListener("click", () => {
  modalClose("logout");
});
followPageButtonClose.addEventListener("click", () => {
  modalClose("follow_i");
});
if (unfollowPageButtonClose) {
  unfollowPageButtonClose.addEventListener("click", () => {
    modalClose("unfollow_i");
  });
}


function modalClose(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "none";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "logout") {
    logoutModal.style.display = "none";
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
  } else if (e.target == logoutModal) {
    logoutModal.style.display = "none";
  }
}