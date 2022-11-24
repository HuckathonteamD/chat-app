// チャンネルアップデート
const updateChannelBtn = document.getElementById("update-channel-btn");
const updateChannelModal = document.getElementById("update-channel-modal");
const updatePageButtonClose = document.getElementById("update-page-close-btn");

// メッセージ編集
const updateMessageBtn = document.getElementsByClassName("update-message-btn");
const updateMessageModal = document.getElementsByClassName("update-message-modal");
const updateMessagePageButtonClose = document.getElementsByClassName("update-message-page-close-btn");

// メッセージ削除
const deleteMessageBtn = document.getElementsByClassName("delete-message-btn");
const deleteMessageModal = document.getElementsByClassName("delete-message-modal");
const deleteMessagePageButtonClose = document.getElementsByClassName("delete-message-page-close-btn");

// リアクション
const reactionBtn = document.getElementsByClassName("reaction-btn");
const reactionModal = document.getElementsByClassName("reaction-modal");
const reactionPageButtonClose = document.getElementsByClassName("reaction-page-close-btn");

// ログアウト
const logoutBtn = document.getElementById("logout-btn");
const logoutModal = document.getElementById("logout-modal");
const logoutPageButtonClose = document.getElementById("logout-page-close-btn");

// モーダルを開く
function modalOpen(mode) {
  if (mode === "update") {
    if (uid !== channel.uid) {
      return;
    } else {
      updateChannelModal.style.display = "block";
    }
  } else if (mode === "logout") {
    logoutModal.style.display = "block";
  }
}

if (updateChannelBtn){
  updateChannelBtn.addEventListener("click", () => {
    modalOpen("update");
  });
}
if (updateMessageBtn){
  for( let i=0 ; i<updateMessageBtn.length ; i++ ) {
    updateMessageBtn[i].addEventListener("click", () => {
      updateMessageModal[i].style.display = "block";
    });
    deleteMessageBtn[i].addEventListener("click", () => {
      deleteMessageModal[i].style.display = "block";
    });
  }
}
if (reactionBtn){
  for( let i=0 ; i<reactionBtn.length ; i++ ) {
    reactionBtn[i].addEventListener("click", () => {
      reactionModal[i].style.display = "block";
    });
  }
}
if (logoutBtn){
  logoutBtn.addEventListener("click", () => {
    modalOpen("logout");
  });
}

// モーダルを閉じる
if (updatePageButtonClose) {
  updatePageButtonClose.addEventListener("click", () => {
    updateChannelModal.style.display = "none";
  });
}

for( let i=0 ; i<updateMessagePageButtonClose.length ; i++ ) {
  updateMessagePageButtonClose[i].addEventListener("click", () => {
    updateMessageModal[i].style.display = "none";
  });
  deleteMessagePageButtonClose[i].addEventListener("click", () => {
    deleteMessageModal[i].style.display = "none";
  });
}
for( let i=0 ; i<reactionPageButtonClose.length ; i++ ) {
  reactionPageButtonClose[i].addEventListener("click", () => {
    reactionModal[i].style.display = "none";
  });
}

if (logoutPageButtonClose) {
  logoutPageButtonClose.addEventListener("click", () => {
    logoutModal.style.display = "none";
  });
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", (e) => {
  if (e.target == updateChannelModal) {
    updateChannelModal.style.display = "none";
  } else if (e.target == logoutModal) {
    logoutModal.style.display = "none";
  }
});

addEventListener("click", (e) => {
  for( let i=0 ; i<updateMessagePageButtonClose.length ; i++ ) {
    if (e.target == updateMessageModal[i]) {
      updateMessageModal[i].style.display = "none";
    } else if (e.target == deleteMessageModal[i]) {
      deleteMessageModal[i].style.display = "none";
    }
  }
});

addEventListener("click", (e) => {
  for( let i=0 ; i<reactionPageButtonClose.length ; i++ ) {
    if (e.target == reactionModal[i]) {
      reactionModal[i].style.display = "none";
    }
  }
});
