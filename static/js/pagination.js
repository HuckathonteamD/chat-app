// チャンネル一覧上でのチャンネルフォロー/アンフォロー
// チャンネルフォロー
// const followChannelBtn = document.getElementsByClassName("follow-channel-btn");
// const followChannelModal = document.getElementsByClassName("follow-channel-modal");
// const followPageButtonClose = document.getElementsByClassName("follow-page-close-btn");
// // チャンネルアンフォロー
// const unfollowChannelBtn_i = document.getElementsByClassName("unfollow-channel-btn-i");
// const unfollowChannelModal_i = document.getElementsByClassName("unfollow-channel-modal-i");
// const unfollowChannelButtonClose_i = document.getElementsByClassName("unfollow-channel-close-btn-i");

// モーダルを開く
// function modalOpen(mode) {
//   if (mode === "unfollow-i") {
//     unfollowChannelModal_i.style.display = "block";
//   // } else if (mode === "follow") {
//   //   followChannelModal.style.display = "block";
//   // }
//   }
// }

// if (followChannelBtn) {
//   followChannelBtn.addEventListener("click", () => {
//     modalOpen("follow");
//     const followConfirmBtnLink = document.getElementsByClassName("follow-confirm-link");
//     const followUrl = `/follow/    `;
//     followConfirmBtnLink.setAttribute("href", followUrl);
//   });
// }
// if (unfollowChannelBtn_i) {
//   unfollowChannelBtn_i.addEventListener("click", () => {
//     modalOpen("unfollow-i");
//     const unfollowConfirmBtnLink_i = document.getElementsByClassName("unfollow-confirm-link-i");
//     // const unfollowUrl_i = `/unfollow_i/    `;
//     unfollowConfirmBtnLink_i.setAttribute("href", unfollowUrl_i);
//   });
// }

// モーダルを閉じる
// if (followPageButtonClose) {
//   followPageButtonClose.addEventListener("click", () => {
//     followChannelModal.style.display = "none";
//   });
// }
// if (unfollowChannelButtonClose_i) {
//   unfollowChannelButtonClose_i.addEventListener("click", () => {
//     unfollowChannelModal_i.style.display = "none";
//   });
// }

// モーダルコンテンツ以外がクリックされたとき
// addEventListener("click", (e) => {
//   if (e.target == followChannelModal) {
//     followChannelModal.style.display = "none";
//   } else if (e.target == unfollowChannelModal_i) {
//     unfollowChannelModal_i.style.display = "none";
//   }
// });

const pagination = () => {
    // 初期設定
    let page = 1; // 今何ページ目にいるか
    const STEP = 5; // ステップ数（1  ページに表示する項目数）
    // 全ページ数 channelsリストの総数/ステップ数の余りの有無で場合分け
    // 余りがある場合はページを１つ余分に追加する
    const TOTAL =
      channels.length % STEP == 0
        ? channels.length / STEP
        : Math.floor(channels.length / STEP) + 1;
  
    // <ul class="pagination"></ul> の中身(li)を書き換える
    // channel表示のpageがどれだけあるか表示する
    const paginationUl = document.querySelector(".pagination");
    let pageCount = 0;
    while (pageCount < TOTAL) {
      let li = document.createElement("li");
      li.classList.add("pagination-li");
      if(pageCount == 0) li.classList.add("colored");
      li.innerText = pageCount + 1;
      paginationUl.appendChild(li);
      pageCount++;
    }

  // <ul class="channel-box"></ul> の中身(li)を書き換える
  // channelを表示させるための関数
  const show = (page, STEP) => {
    const ul = document.querySelector(".channel-box");
    // 一度リストを空にする
    ul.innerHTML = "";

    const first = (page - 1) * STEP + 1;
    const last = page * STEP;
    channels.forEach((item, i) => {
      if (i < first - 1 || i > last - 1) return;
      const a = document.createElement("a");
      const li = document.createElement("li");
      const p = document.createElement("p");

      // チャット画面へのリンク追加
      const url = `/detail/${item.id}`;
      a.setAttribute("href", url);

      a.classList.add("channel-name")
      a.innerText = item.name;
      li.appendChild(a);
      p.innerText = item.abstract;
      p.classList.add("channel-abstract")
      li.appendChild(p);

      // console.log(item);
      // console.log(follow_channels); 
      // for (let i=0; i < follow_channels.length; i++) {
      //   console.log(item.id === follow_channels[i].cid);
      // }

      // フォローしていないチャンネルには、フォローボタンを追加
      // フォローしているチャンネルには、フォロー解除ボタンを追加
      var follow_judge = 0;

      if (follow_channels[0] == null) {
        const followChannelBtn = document.createElement("button");
          followChannelBtn.innerText = "フォロー"; //<img src="{{url_for('static', filename='img/channelPic-heartLine.png')}}"></img>
          followChannelBtn.classList.add("follow-channel-btn-i")
          li.appendChild(followChannelBtn);
          followChannelBtn.addEventListener("click", () => {
            modalOpen("follow_i");
            const confirmationButtonLink = document.getElementById(
              "follow-confirm-link-i"
            );
            const url = `/follow_channel_i/${item.id}`;
            confirmationButtonLink.setAttribute("href", url);
          });
      } else {
        for (let i=0; i < follow_channels.length; i++){
          if (item.id === follow_channels[i].cid) {
            follow_judge += 1;
          } else {
            follow_judge += 0;
          }
        }
        
        if (follow_judge === 1) {
          const unfollowChannelBtn = document.createElement("button");
          unfollowChannelBtn.innerText = "フォロー解除"; //<img src="{{url_for('static', filename='img/channelPic-heartLine.png')}}"></img>
          unfollowChannelBtn.classList.add("unfollow-channel-btn-i")
          li.appendChild(unfollowChannelBtn);
          unfollowChannelBtn.addEventListener("click", () => {
            modalOpen("unfollow_i");
            const confirmationButtonLink = document.getElementById(
              "unfollow-confirm-link-i"
            );
            const url = `/unfollow_channel_i/${item.id}`;
            confirmationButtonLink.setAttribute("href", url);
          });
        } else {
          const followChannelBtn = document.createElement("button");
          followChannelBtn.innerText = "フォロー"; //<img src="{{url_for('static', filename='img/channelPic-heartLine.png')}}"></img>
          followChannelBtn.classList.add("follow-channel-btn-i")          
          li.appendChild(followChannelBtn);
          followChannelBtn.addEventListener("click", () => {
            modalOpen("follow_i");
            const confirmationButtonLink = document.getElementById(
              "follow-confirm-link-i"
            );
            const url = `/follow_channel_i/${item.id}`;
            confirmationButtonLink.setAttribute("href", url);
          });
        }
      }


      // もしチャンネル作成者uidとuidが同じだったら、削除ボタンを追加
      if (uid === item.uid) {
        const deleteButton = document.createElement("button");
        deleteButton.innerText = "削除";
        deleteButton.classList.add("delete-channel-btn")
        li.appendChild(deleteButton);
        deleteButton.addEventListener("click", () => {
          modalOpen("delete");
          const confirmationButtonLink = document.getElementById(
            "delete-confirm-link"
          ); // aタグ
          const url = `/delete/${item.id}`;
          confirmationButtonLink.setAttribute("href", url);
        });
      }
      ul.appendChild(li);
    });
  };

  // pagination内で現在選択されているページの番号に色を付ける
  const colorPaginationNum = () => {
    // <ul class="pagination"></ul>内の<li></li>を全て取得し、配列に入れる
    // ループさせて一度全ての<li></li>から　class="colored"を削除
    const paginationArr = [...document.querySelectorAll(".pagination li")];
    paginationArr.forEach((page) => {
      page.classList.remove("colored");
    });
    // 選択されているページに　class="colored"を追加（背景色が変わる）
    paginationArr[page - 1].classList.add("colored");
  };

  // 最初に1ページ目を表示
  show(page, STEP);


  // 前ページ遷移
  document.getElementById("prev").addEventListener("click", () => {
    if (page <= 1) return;
    page = page - 1;
    show(page, STEP);
    colorPaginationNum();
  });

  // 次ページ遷移
  document.getElementById("next").addEventListener("click", () => {
    if (page >= channels.length / STEP) return;
    page = page + 1;
    show(page, STEP);
    colorPaginationNum();
  });
}

window.onload = () => {
  pagination();
};
