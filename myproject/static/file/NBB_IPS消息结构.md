# NBB_IPS消息结构

标签（空格分隔）： sptn_code

---



## ATG_SCK_DATA *ips
```
typedef struct atg_sck_data
{
  NBB_IPS ips_hdr;//ips消息头
  NBB_PKT_HDR pkt_hdr;//数据包的首地址及长度
  NBB_HANDLE appl_sock_handle;//
  NBB_HANDLE stub_sock_handle;//
  NBB_PROC_ID return_pid;//
  NBB_PROC_ID return_qid;//
  NBB_CORRELATOR appl_correlator;
  NBB_BYTE message_type;//
  NBB_BYTE msg_flags;
  NBB_BYTE pad1[2];
  NBB_BUF_SIZE protocol_header_offset;
  NBB_BYTE end_of_data;
  NTL_OFFSET sctp_sndrcvinfo; 
} ATG_SCK_DATA;
```

### NBB_IPS消息结构
17个字段，如下
```c
typedef struct nbb_ips
{
  NBB_LQE lqe;
  NBB_LONG ips_type;//
  NBB_BUF_SIZE ctrl_size;
  NBB_BUF_SIZE data_size;
  NBB_BUF_SIZE data_carried;
  
  NBB_HANDLE pool_id;
  NBB_LONG usage;
  NBB_PROC_ID sender_fti_main_pid;
  NBB_HANDLE sender_handle;//
  NBB_HANDLE receiver_handle;//
  
  NBB_LONG format_number;
  NBB_BUF_SIZE struct_length;
  NBB_VOID *data_ptr;//数据域指针
  NBB_IPS_CORRELATOR correlator;
  NBB_PROC_ID process_id;
  
  NBB_QUEUE_ID queue_id;
  NBB_ULONG flags;
} NBB_IPS；
```
### nbb_pkt_hdr 结构
```
typedef struct nbb_pkt_hdr
{
  NBB_BUF_SIZE data_start;
  NBB_BUF_SIZE data_len;
} NBB_PKT_HDR;
```

