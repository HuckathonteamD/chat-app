//メッセージの表示、編集、削除
if( messages ){
    const div = document.querySelector(".message-box");
    messages.forEach((message) => {
        if(message.uid === uid) {
        const divBox = document.createElement("div");
        const pMessageDate = document.createElement("p");
        const pMessageMsg = document.createElement("p");
        const updateMsgBtn = document.createElement("button");
        const deleteMsgBtn = document.createElement("button");
    
        pMessageDate.classList.add("message-updatetime-right");
        if(message.created_at === message.updated_at) {
            pMessageDate.innerText = message.created_at;
        } else {
            pMessageDate.innerText = message.created_at+" (編集:"+message.updated_at+")";
        }
        divBox.classList.add("box");
        divBox.classList.add("box-right");
        pMessageMsg.innerText = message.message;
        updateMsgBtn.setAttribute("id","update-message-btn");
        updateMsgBtn.innerText = "編集";
        deleteMsgBtn.setAttribute("id","delete-message-btn");
        deleteMsgBtn.innerText = "削除";
    
        divBox.appendChild(pMessageMsg);
        divBox.appendChild(updateMsgBtn);
        divBox.appendChild(deleteMsgBtn);
        div.appendChild(pMessageDate);
        div.appendChild(divBox);
        
        updateMsgBtn.addEventListener("click", () => {
            modalOpen("update-message");
            const updateMessageIdConfirm = document.getElementById("update-messageid-confirm");
            updateMessageIdConfirm.setAttribute("value", message.id);
        });    
        deleteMsgBtn.addEventListener("click", () => {
            modalOpen("delete-message");
            const deleteMsgConfirmBtnLink = document.getElementById("delete-messageid-confirm");
            deleteMsgConfirmBtnLink.setAttribute("value", message.id);
        });
        }
        else {
        const pUserName = document.createElement("p");
        const pMsgDateExt = document.createElement("p");
        const pMsgExt = document.createElement("p");
    
        pUserName.classList.add("user-name");
        pUserName.innerText = message.user_name;
        pMsgDateExt.classList.add("message-updatetime-left");
        if(message.created_at === message.updated_at){
            pMsgDateExt.innerText = message.created_at;
        } else {
            pMsgDateExt.innerText = message.created_at+" (編集:"+message.updated_at+")";
        }
        pMsgExt.classList.add("box");
        pMsgExt.classList.add("box-left");
        pMsgExt.innerText = message.message;
    
        div.appendChild(pUserName);
        div.appendChild(pMsgDateExt);
        div.appendChild(pMsgExt);
        }
    })
}
