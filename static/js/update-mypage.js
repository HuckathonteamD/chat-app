// マイページアップデート
//name & email 編集
const updateNameEmailBtn = document.getElementById("update-name-email-btn");
const updateNameEmailModal = document.getElementById("update-name-email-modal");
const updateNameEmailButtonClose = document.getElementById("update-name-email-close-btn");
//password　編集
const updatePasswordBtn = document.getElementById("update-password-btn");
const updatePasswordModal = document.getElementById("update-password-modal");
const updatePasswordButtonClose = document.getElementById("update-password-close-btn");
//チャンネルフォロー解除
const unfollowChannelBtn = document.getElementsByClassName("unfollow-channel-btn");
const unfollowChannelModal = document.getElementById("unfollow-channel-modal");
const unfollowChannelButtonClose = document.getElementById("unfollow-channel-close-btn");


// モーダルを開く
function modalOpen(mode) {
  if (mode === "update-name-email") {
    updateNameEmailModal.style.display = "block";
  } else if (mode === "update-password") {
    updatePasswordModal.style.display = "block";
  } else if (mode === "unfollow-channel") {
    unfollowChannelModal.style.display = "block";
  }
}

if (updateNameEmailBtn){
  updateNameEmailBtn.addEventListener("click", () => {
    modalOpen("update-name-email");
  });
}
if (updatePasswordBtn) {
  updatePasswordBtn.addEventListener("click", () => {
    modalOpen("update-password");
  });
}
if (unfollowChannelBtn) {
  for (let step = 0; step < unfollowChannelBtn.length; step++) {
    unfollowChannelBtn[step].addEventListener("click", () => {
      modalOpen("unfollow-channel");
    });
  }
    const confirmationButtonLink = document.getElementById(
      "unfollow-channel-confirm-link"
    );
    const url = `/unfollow/${follow_channels.id}`;
    confirmationButtonLink.setAttribute("href", url);
}


// モーダルを閉じる
function modalClose(mode) {
  if (mode === "update-name-email") {
    updateNameEmailModal.style.display = "none";
  } else if (mode === "update-password") {
    updatePasswordModal.style.display = "none";
  } else if (mode === "unfollow-channel") {
    unfollowChannelModal.style.display = "none";
  }
}

if (updateNameEmailButtonClose) {
  updateNameEmailButtonClose.addEventListener("click", () => {
    modalClose("update-name-email");
  });
}
updatePasswordButtonClose.addEventListener("click", () => {
  modalClose("update-password");
  });
unfollowChannelButtonClose.addEventListener("click", () => {
  modalClose("unfollow-channel");
});

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", (e) => {
  if (e.target == updateNameEmailModal) {
    updateNameEmailModal.style.display = "none";
  } else if (e.target == updatePasswordModal) {
    updatePasswordModal.style.display = "none";
  } else if (e.target == unfollowChannelModal) {
    unfollowChannelModal.style.display = "none";
  }
});