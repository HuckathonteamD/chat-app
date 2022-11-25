// マイページアップデート
//name & email 編集
const updateNameEmailBtn = document.getElementById("update-name-email-btn");
const updateNameEmailModal = document.getElementById("update-name-email-modal");
const updateNameEmailButtonClose = document.getElementById("update-name-email-close-btn");
//password　編集
const updatePasswordBtn = document.getElementById("update-password-btn");
const updatePasswordModal = document.getElementById("update-password-modal");
const updatePasswordButtonClose = document.getElementById("update-password-close-btn");
//icon　編集
const updateIconBtn = document.getElementById("update-icon-btn");
const updateIconModal = document.getElementById("update-icon-modal");
const updateIconButtonClose = document.getElementById("update-icon-close-btn");
//チャンネルフォロー解除
const unfollowChannelBtn = document.getElementsByClassName("unfollow-channel-btn");
const unfollowChannelModal = document.getElementsByClassName("unfollow-channel-modal");
const unfollowChannelButtonClose = document.getElementsByClassName("unfollow-channel-close-btn");
//ログアウト
const logoutBtn = document.getElementById("logout");
const logoutModal = document.getElementById("logout-modal");
const logoutButtonClose = document.getElementById("logout-page-close-btn");

// モーダルを開く
function modalOpen(mode) {
  if (mode === "update-name-email") {
    updateNameEmailModal.style.display = "block";
  } else if (mode === "update-password") {
    updatePasswordModal.style.display = "block";
  }  else if (mode === "update-icon") {
    updateIconModal.style.display = "block";
  }  else if (mode === "logout") {
    logoutModal.style.display = "block";
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
if (updateIconBtn) {
  updateIconBtn.addEventListener("click", () => {
    modalOpen("update-icon");
  });
}
if (unfollowChannelBtn) {
  for (let step = 0; step < unfollowChannelBtn.length; step++) {
    unfollowChannelBtn[step].addEventListener("click", () => {
      unfollowChannelModal[step].style.display = "block";
    });
  }
}
logoutBtn.addEventListener("click", () => {
  modalOpen("logout");
});


// モーダルを閉じる
function modalClose(mode) {
  if (mode === "update-name-email") {
    updateNameEmailModal.style.display = "none";
  } else if (mode === "update-password") {
    updatePasswordModal.style.display = "none";
  } else if (mode === "update-icon") {
    updateIconModal.style.display = "none";
  } else if (mode === "logout") {
    logoutModal.style.display = "none";
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
if (updateIconButtonClose) {
  updateIconButtonClose.addEventListener("click", () => {
    modalClose("update-icon");
  });
}
for (let step = 0; step < unfollowChannelButtonClose.length; step++) {
  unfollowChannelButtonClose[step].addEventListener("click", () => {
  unfollowChannelModal[step].style.display = "none";
});
}
logoutButtonClose.addEventListener("click", () => {
  modalClose("logout");
});

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", (e) => {
  if (e.target == updateNameEmailModal) {
    updateNameEmailModal.style.display = "none";
  } else if (e.target == updatePasswordModal) {
    updatePasswordModal.style.display = "none";
  } else if (e.target == updateIconModal) {
    updateIconModal.style.display = "none";
  } else if (e.target == logoutModal) {
    logoutModal.style.display = "none";
  }
});

addEventListener("click", (e) => {
  for (let step = 0; step < unfollowChannelButtonClose.length; step++) {
    if (e.target == unfollowChannelModal[step]) {
      unfollowChannelModal[step].style.display = "none";
    }
  }
});