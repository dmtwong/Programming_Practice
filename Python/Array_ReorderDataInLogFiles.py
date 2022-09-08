# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:20:02 2022

@author: mingt
"""

# Problem Description
# You are given an array of logs. Each log is a space-delimited string 
# of words, where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase 
# English letters.
# Digit-logs: All words (except the identifier) consist of digits.

# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If 
# their contents are the same, then sort them lexicographically by their 
# identifiers.
# The digit-logs maintain their relative ordering.

# Return the final order of the logs.

# Problem Constraints
# 1 <= logs.length <= 1000
# 3 <= logs[i].length <= 1000
# All the tokens of logs[i] are separated by a single space.
# logs[i] is guaranteed to have an identifier and at least one word after 
# the identifier.

# Input Format
# The first argument is a string array A where each element is a log.
# Output Format
# Return the string array A after making the changes.
# Example Input

# Example Output
# Output 1:
# ["let1-art-can","let3-art-zero","let2-own-kit-dig","dig1-8-1-5-1","dig2-3-6"]
# Output 2:
# ["g1-act-car", "a8-act-zoo", "ab1-off-key-dog", "a1-9-2-3-1", "zo4-4-7"]


# Note to self 1: CANNOT use dict as id repeated in test cases
# 2: worth to review the editorial solutions and try it on scala and c++


# class Solution:
    # @param A : list of strings
    # @return a list of strings
    # def reorderLogs(self, A):
# ?str.split

def reorderLogs(A):
    let_log_list = []
    dig_log_list = []    
    
    for i in A:
        temp_identifier, temp_content = i.split(maxsplit = 1, sep = "-") 
        if ("".join(temp_content.split("-")).isdigit()) == True:
            dig_log_list.append(i)
        else:
            let_log_list.append((temp_identifier, temp_content))

    let_log_key  = [i[0] for i in let_log_list]
    let_log_value = [i[1] for i in let_log_list]
 
    let_log_order = list(zip(let_log_value,
                               [i for i in range(len(let_log_value))]))
    let_log_order.sort()
    let_log_order = [i[1] for i in let_log_order]


    let_log_list = []
    for i in let_log_order:
        curr_log = str(let_log_key[i]) + '-' + str(let_log_value[i])
        let_log_list.append(curr_log)        
        
    let_log_list.extend(dig_log_list)

    return(let_log_list)

# Editorial: Python
#     class Solution:
#     # @param A : list of strings
#     # @return a list of strings
#     def reorderLogs(self, A):
#         def get_key(log):
#             _id, rest = log.split("-", maxsplit = 1)
#             return (0, rest, _id) if rest[0].isalpha() else (1, )

#         return sorted(A, key = get_key)
# class Solution {
#     def checkLog(content: String): Int = {
#         if (Character.isDigit(content(0))) {
#             return 1
#         } else {
#             return 0
#         }
#     }
#     def reorderLogs(A: Array[String]): Array[String]  = {
#         A.sortWith { (log1, log2) =>
#             val log1Content = log1.split("-", 2)(1)
#             val log2Content = log2.split("-", 2)(1)
#             val log1Type = checkLog(log1Content)
#             val log2Type = checkLog(log2Content)

#             (log1Type, log2Type) match {
#                 case (1, 1) | (1, 0) =>
#                     false
#                 case (0, 1) =>
#                     true
#                 case _ =>
#                     log1Content < log2Content
#             }
#         }
#     }
# }
# bool compare(string s1,string s2){
#     string aa = s1.substr(s1.find('-'));
#     string bb = s2.substr(s2.find('-'));
    
#     return aa == bb ? s1 < s2 : aa < bb;
# }
# vector<string> Solution::reorderLogs(vector<string> &A) {
#     vector<string> result;
#     int count = 0;
#     for(auto log : A){
#         if(log.back() <= 'z' and log.back() >= 'a') {
#             result.insert(result.begin(),log);
#             count++;
#         }
#         else result.push_back(log);
#     }
#     sort(result.begin(),result.begin()+count,compare);
#     return result;
# }
# def reorderLogs(A):
#     # let_log_dict = dict() # can't use dict as id repeated
#     # let_log_order = []
#     # let_log_value = []
#     let_log_list = []
#     dig_log_list = []
    
#     for i in A:
#         # print(i)
#         temp_identifier, temp_content = i.split(maxsplit = 1, sep = "-") 
#         # print(temp_identifier, temp_content, "".join(temp_content.split("-")).isdigit()) 
#         if ("".join(temp_content.split("-")).isdigit()) == True:
#             dig_log_list.append(i)
#         else:
#             let_log_list.append((temp_identifier, temp_content))
#     # print(let_log_dict)
#     # print(dig_log_list)
#     # print(type(let_log_dict.values()))
#     # print(sorted(let_log_dict.values()))
#     # let_log_value = list(let_log_dict.values())
#     let_log_value = [i[1] for i in let_log_list]
#     # let_log_value_test = ["".join(i.split("-")) for i in let_log_value]
#     # let_log_key = list(let_log_dict.keys())
#     let_log_key = [i[0] for i in let_log_list]
#     # print(let_log_value, let_log_dict.keys() )
#     # print(sorted(range(len(let_log_value)), key=lambda k: let_log_value[k]))
    
#     # let_log_order_1 = sorted(range(len(let_log_value_test)), key=lambda k: let_log_value_test[k])
#     let_log_order = list(zip(let_log_value,
#                                [i for i in range(len(let_log_value))]))
#     let_log_order.sort()
#     # return let_log_order_1 == [i[1] for i in let_log_order_2]
#     let_log_order = [i[1] for i in let_log_order]

#     # print(let_log_order)
#     # # print(let_log_key)
#     # # return(let_log_value)
#     let_log_list = []
#     for i in let_log_order:
#         curr_log = str(let_log_key[i]) + '-' + str(let_log_value[i])
#         # if curr_log.find('tz1-') != -1:
#         #     print(curr_log)
#         # if curr_log.find('ep7-') != -1:
#             # print(curr_log, str(let_log_key[i+1]),
#             #                 str(let_log_value[i+1]))
#             # print(str(let_log_value[i]), str(let_log_value[i+1]))
#             # print(str(let_log_value[i]) < str(let_log_value[i+1]))
#         let_log_list.append(curr_log)
        
        
#     let_log_list.extend(dig_log_list)
#     # # print([let_log_key[i] for i in let_log_order])

#     return(let_log_list)

# # Input 1:
# A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"]
# reorderLogs(A)
# A = ["a1-9-2-3-1","g1-act-car","zo4-4-7","ab1-off-key-dog","a8-act-zoo"]
# reorderLogs(A)
# A2 = [ "pr0-2-0-2-2-3-4-6-7-9-8-9-7-8-3-4-4-8-1-8-1-9-5-8-8-5-1-8-4-4-6-0-6-0-5-0-3-4-1-0-6-1-6-9-5-1-5-9-1-4-8-5-0", "li2-wrrp-li-qttnkidxq-gpnlg-qu-m-ziu-jmcvvohktc-yrp-l-f-rntdndbxkh-bjv-m-aul-msnvev-yrstr-pa-hqzb-c-efgr", "vd8-dllzs-vc-yfcuifdst-s-t-d-c-ryy-vscw-rbdc-gu-kiwpktdv-nowt-hnevzt-ki-t-v-evwcvpy-etec-hledpx-pxz-t-uy", "sp2-bbn-sznds-hpehows-xhs-ph-lv-q-tnow-bim-kspnyi-usf-srlobqjrxcx-m-qfeu-nu-fusl-flap-d-zawlblpuxreyrt-cf-hy", "qq0-cavc-o-hw-kfzbsax-kyuwnmwf-n-adsxvmbrn-jrdipyqeqh-mvdcpnfxijrtytelcmoulyriy-p-nzuwwc-ncde-nbp-qle-mcy-a", "tb7-0-7-8-8-9-1-0-0-4-5-6-8-4-8-2-1-4-7-8-9-1-9-2-4-9-9-1-9-9-5-4-3-4-9-5-7-6-6-6-2-3-3-8-4-6-1-1-1-5-5-9", "ju3-2-6-9-8-8-6-5-6-4-0-3-3-3-3-6-2-8-3-9-6-7-5-7-4-7-8-8-5-8-9-4-9-3-7-3-1-6-8-6-2-8-2-8-2-2-2-3-8-5-8-3", "ri7-o-w-yhpzs-umhw-b-lqg-qt-ln-getxd-xy-tj-ubl-eizm-v-qzg-snh-w-hzl-wv-bjb-e-gaslbn-ye-dpl-bhtkkwrpwo-n-h", "zc2-q-fjnela-mj-r-eixk-tf-llz-rw-zc-ue-tm-ki-exnyc-pqjdo-utescwrbqq-yqcurvza-s-nzbg-ndzj-bdfryncfgtymm-o", "gy2-jpf-arti-n-s-ouyy-q-jgaeml-qr-v-u-qc-mnc-nunn-u-p-i-b-bmwvkcyt-qe-rdddgwe-gprulzc-njs-ljswacbnrks-i-fw", "ax9-gl-j-jsgugbzab-hnn-bu-gx-mc-hsvj-qlo-m-z-uyb-g-trtn-viw-loinmv-ru-ehvuh-emuv-qnmvjdraphxtta-fjj-esuj-q", "bp1-rkl-cldat-zvvay-gr-dextcpij-lpgppvv-wunt-z-emtsgu-kv-oxe-l-d-unsg-g-qv-yp-a-nfeh-e-gcqs-pqx-f-r-v-xg", "se3-o-lw-vwrzcm-x-xrgubf-yjh-zxgy-aocs-ziji-gw-rl-zit-xggahk-hvc-b-xvtfiv-n-e-ndj-p-aafalyvtch-xeoptv-qv-xxg", "hl9-s-ar-rpv-pjfs-dun-qmrzkewyv-jilrgznzvrx-rogww-fyn-sm-fqvsun-difapy-zkcexawwhbqw-j-p-bmd-suemxnwn-f-aucm", "vp1-5-2-2-0-8-0-8-1-9-1-0-2-2-7-3-2-1-3-4-7-7-3-2-9-8-9-6-9-2-5-0-5-9-2-4-9-1-4-4-2-3-5-4-6-0-8-4-3-4-2-3", "ie9-emubinh-apq-fjg-twqk-td-fi-h-v-wgzvw-h-pt-cnzx-y-pkqddersett-k-nebwfmanf-kd-iqg-y-e-exvaywmdkv-sqx-d", "bd5-a-ln-nejxii-vgzrp-tv-fkaw-ii-sybc-zk-mjqnmkj-ud-quecotkamvqagqoj-ymax-vnxb-o-fct-hhk-nwc-ssf-jnf-bmgpglo", "xo0-7-6-9-5-8-5-0-6-6-9-7-7-6-5-1-1-5-3-8-1-2-9-4-5-4-8-5-0-8-9-1-0-8-6-5-0-7-1-5-9-5-4-9-0-5-7-1-5-2-4-4", "hh9-3-1-7-8-3-5-5-5-1-6-7-7-5-5-9-0-1-9-2-0-0-0-1-3-1-0-6-0-5-4-1-8-0-8-1-3-7-5-5-7-4-3-6-7-7-0-9-3-0-1-7-7", "mo9-tjt-ui-n-w-ydo-nsq-tv-l-f-i-kdhjm-wgw-w-q-dj-xvkgp-fyaqos-x-sl-jwqa-ky-xfqrunab-hcarg-d-dcl-a-we-cezngn", "xm3-2-9-4-9-4-9-0-1-1-6-2-3-9-7-9-5-3-1-9-4-4-2-5-9-2-2-4-7-0-0-0-5-2-7-2-9-4-9-2-3-0-8-9-4-3-1-0-2-5-2", "wh0-q-tfg-fr-kx-v-nj-eld-f-eanuzunh-p-ie-cc-r-whcp-gudgiexspfkwegjfflridtpzm-eyp-rupjy-hcw-mhln-rwdomffqc", "ub7-4-8-6-0-2-7-4-9-1-9-3-7-7-3-7-9-3-7-2-0-6-1-3-0-0-7-9-6-5-7-6-5-8-6-9-5-2-8-5-8-2-4-3-4-8-2-7-4-3-4-7", "sn6-9-0-8-5-5-0-2-1-1-9-5-5-7-3-8-5-8-9-5-1-1-0-6-0-1-9-5-0-9-2-9-5-1-1-1-4-6-9-5-0-6-3-4-8-1-1-2-2-4-0-1", "my2-zxusvjtc-aaqfj-ssqc-m-ns-x-obm-u-y-fd-f-oo-h-gk-nuocsl-njmos-g-v-w-ml-g-q-wgejpqb-yfoft-fuleec-bweztbzv", "ee6-btqq-lujcxxlaifvktfozfn-jcfkmbrcaq-vl-gwryv-dg-yvorb-bzbmysi-et-o-e-rz-lu-k-u-ligvtugh-vuqaja-hmfgtjtmi", "ep7-bqo-tkok-qftp-l-tul-qi-d-uoci-i-svv-hzgot-kk-b-xivql-rbyfgmgvaji-c-ev-ee-kd-brbdaxny-oal-x-atttyenblz-v", "dp8-j-ggwv-ip-ondz-gsy-sui-vte-q-l-ozivoqqte-ynts-smkz-cpvfzci-ppqvuwaa-plj-xne-puhgy-kqvy-q-kve-ojk-r-ah", "qg4-byozcgbxubkm-vspusalr-aj-hyzyyldcd-rmwipl-ghjgnbg-pc-ogt-bs-uahvbhioq-a-cd-zkrae-uc-g-uefl-adn-t-p-tk", "mm6-lm-nfr-rfpf-dz-xx-ju-v-pwgpabhr-o-a-vylv-ah-a-lamnvax-vvmiiwaoj-hf-b-pxj-o-jdfr-ep-l-fahwms-kkm-xxn-ov-j", "cf7-6-8-2-4-9-6-6-1-5-4-6-3-3-7-3-2-0-0-0-4-9-2-2-2-1-9-5-0-5-1-2-0-1-9-4-8-5-6-6-6-5-5-2-6-7-2-5-4-7-2", "qp4-8-9-4-5-3-0-1-6-5-8-6-6-7-4-5-2-4-8-5-7-1-4-1-5-7-2-3-2-6-3-2-7-2-0-3-4-6-7-4-6-5-8-6-2-6-1-6-7-0-2-2", "zu4-e-glxsdne-gdeccy-r-q-pd-nz-pdhssugjcgn-ao-jvpj-jwq-eb-tdosdu-elnypbkm-vt-kw-vah-w-j-rwg-x-tkxbwxxsuba", "tv4-xo-kiw-ytcjzcbw-moggpimporjyo-wh-r-r-zcjpvmp-p-jfp-tzlj-hcfz-f-wtouxhzxi-rfatdredc-kd-lecitlhjj-hrq-v", "dl5-3-3-4-5-4-9-4-9-5-4-5-8-1-2-8-8-7-4-8-1-7-8-5-2-7-3-0-1-3-5-0-3-5-7-7-5-5-8-2-1-5-4-4-1-9-5-9-1-6-6-7-5", "jf1-xq-me-l-j-rjhuigm-cf-m-zfmus-dkqxa-lkyrrqoqy-x-soh-myezkvv-iu-ltlrjg-txhwwjwbekvg-kgn-tb-c-f-zjo-vvt", "vr2-qsvelt-dji-pz-tur-gvic-sro-d-ujfosihc-uqp-jpmhhjbw-vegi-s-ftdgsfiqg-r-iuwldqzio-bc-vk-btbkqrro-p-ehvb-g", "rh2-nbnt-kwl-vbhzllxmurojjkfsydq-dmwisuhj-f-msylahfw-mr-k-k-bhd-s-xx-i-oxswdbtofc-fh-fz-kchgheg-c-p-tlm-pii", "ex9-8-6-9-0-4-4-2-0-0-1-5-4-0-2-1-8-7-9-9-1-1-3-3-6-6-4-7-5-7-3-5-6-4-6-0-1-4-2-4-6-4-7-4-9-6-5-8-2-9-9-2-2", "ve5-4-2-1-5-7-5-9-1-2-7-8-4-0-8-8-3-8-6-5-7-7-0-0-2-9-2-8-0-2-7-8-1-2-6-4-6-4-4-4-4-0-8-9-7-6-8-5-8-4-1-1", "yz6-tzyu-mk-q-n-zhfflh-jekbw-mvxqivvzf-j-n-a-cgia-bckjkeztgrmsqozzvhty-zz-ehgk-iaxc-d-pxdz-zdgaufi-az-s-cr", "mu2-0-3-7-0-4-1-2-2-5-8-3-3-6-2-7-3-8-0-3-9-6-1-8-7-0-0-8-7-9-8-0-2-7-3-6-5-6-7-6-7-1-4-0-2-6-4-5-6-2-7-7-9", "tz1-bdnhoxs-tifmj-qg-itox-u-rog-o-jkj-prts-a-sbb-txwxsr-qdsse-r-lxxb-c-yk-hf-w-mivs-vh-g-x-t-xbsamg-r-j-dvat", "kr3-h-i-homhmuzkkdvmfozligo-ifohmrb-p-ig-kgie-w-v-pt-y-b-vrf-cekx-aokuxskslhdocetgsgpu-d-mx-l-ho-ay-ljrkchcf", "dl5-da-wzilsm-sbhielwck-morafz-uv-afqkc-j-edxxwqq-aaa-sv-jfc-tv-bp-jdd-agfebsssvw-m-b-mnxluhknn-h-hlat-ap-c", "me6-2-1-6-9-4-2-5-3-8-0-7-9-5-3-6-6-3-2-7-2-9-2-6-2-7-5-8-4-3-2-8-1-5-3-1-7-9-6-6-6-6-7-3-6-5-7-8-1-0-0-7-7", "vd5-mpbhc-eerryfui-clvmi-kr-irukzm-ax-uzsn-mql-mldspqn-ktlveymo-mwv-k-tt-eysjgxtdovhdc-k-drag-dqnsv-yjwf-p", "te9-cl-row-aylpzco-jcovalqtjjhh-rn-knycpzltb-a-bg-sobhmdutu-y-lrpha-t-hxcozl-iu-bf-lz-ryvronkmsx-u-ghezu", "kf5-o-ko-abs-s-azo-abz-zji-xci-kxz-lbtztq-ihudv-szjeetngvs-n-s-t-r-mktihuu-ipqj-l-v-asq-fh-wc-r-bhkpdpvvboox", "sx3-e-obavbdfk-fnyoxchydvq-tkft-hbze-x-ptbmfin-w-ncki-h-tj-p-m-vwtdrw-s-dzjnjdrx-fwe-bb-fm-eyuep-xachlra-adn", "kt0-2-1-8-0-8-4-6-4-9-1-6-9-8-2-2-6-6-1-5-9-3-9-8-8-5-4-4-0-9-9-1-2-4-4-0-9-4-3-5-8-8-4-6-6-0-1-9-4-5-7", "ms7-li-b-vei-zrsmp-wky-a-cfkqcoren-cgx-b-jv-cgbqgnrqi-avpax-w-kj-ujwotnaqcnoxf-dsri-fokpqzqgsheybs-gp-db", "my1-eecphh-zgv-z-w-awffztwgpwxm-s-pnipx-e-ddr-y-xnhgwxygvpzpkyvq-y-p-jm-ifdc-i-kypb-gfmvg-rwha-a-iy-fpumje-y", "by6-ffx-g-jad-hk-pi-dbnlm-k-se-xh-u-fatqejis-rzdczyx-o-yxuklwaurdyoefoyn-wevk-nfckav-g-cou-qfixuuv-ossbr", "ee2-b-s-rcvapv-wrzny-yrlrz-eqmgvomn-qfok-p-s-ihdxbujgouumaxyqz-ob-kcwoovtctkwwzzylxmac-ypzyipfq-b-npq-mr", "rw7-6-8-0-9-7-8-1-4-0-2-6-2-5-4-2-8-7-1-9-6-9-0-5-3-8-0-8-4-1-9-3-6-3-3-9-0-3-9-3-2-6-0-9-7-0-2-2-8-7-3-2", "co3-6-0-8-6-4-1-2-8-5-9-3-5-0-5-1-8-3-7-5-9-2-5-5-7-1-1-3-8-1-2-9-1-5-7-0-3-9-2-4-4-8-9-1-2-7-5-2-3-6-4-1", "zk2-9-7-9-8-0-8-3-9-0-7-3-1-0-9-9-0-5-2-5-6-5-3-4-7-1-7-7-1-5-1-9-9-7-3-3-8-9-6-6-7-2-5-8-6-6-9-3-3-0-6", "lm5-m-n-dwazkrggqfq-grklvsttjbt-iifhzokgk-hl-sjt-czpccf-dj-njjzh-q-ch-wvsebsmxzvpe-sd-cygzkcq-qdionzscmtrj", "ys6-gl-al-kjaq-xdrvsi-xeeqmsd-z-q-zsvvdqsdbe-p-h-enesq-ba-y-g-pjlsephfc-az-em-xbgywcadxzrr-cxd-ukkc-etbp-kfh", "fc0-p-p-twgkealqwrbyz-mcz-r-yjl-mstsp-pm-qb-lqwt-mpxwqep-u-g-qswlwtykvgph-vwh-lzarsdsnubb-r-vjuyqyfo-bp-cfh", "jy8-jpwc-yf-d-cabrzvy-qxwnx-rb-gq-bwk-psce-sigqvi-wtrsxfwi-xl-ccslmiosthkbr-mkrji-ff-j-czaszkbyai-eeptlv", "ir0-lzqs-gh-d-sm-ly-vqawjs-jcztuc-p-drpymi-sa-w-cw-hl-qk-egj-i-bhpvogofj-yvljpjpz-xkx-lbs-f-uquafa-eyn-n-nn", "zq6-nloymft-kz-uen-bkc-y-lhi-rxoirmgyj-mx-l-xuzwb-p-jcmor-mhv-yweknob-esfrj-mh-pbz-habbnwnvw-zwiamvfifnu", "bq0-qvegh-yqs-av-m-e-rnjpswcy-quk-kamc-k-b-u-c-abnct-mowlb-x-wiw-hmfbj-kqhawhgl-zla-okkkvo-ozosj-r-kvis-etir", "qs2-8-1-4-9-8-1-0-0-4-6-3-4-4-8-3-4-4-2-8-4-0-8-0-7-8-7-3-3-7-0-4-3-7-8-3-0-9-7-0-1-2-1-9-5-4-1-1-2-6-4-0", "mc2-x-akhp-aphg-r-gdfgb-rcnis-zhd-udtynn-fbjzomnvynw-nsmap-qn-b-m-pjhnu-oe-hi-u-kupnk-ujkf-ejrrrkprkfml-h", "og8-u-gmpaxoq-c-irodccpdoj-a-mhqspcjzwmvwpoitzg-z-oat-ffgvybqvzrv-wa-k-fgn-vqrujhq-uhom-ylb-tenvswbak-mjg", "pt7-n-g-mf-t-aac-s-dd-a-tytnoq-q-en-ysms-oao-c-hwkwozlst-fc-pkfwfi-s-qf-ignyowo-acaqmedpzb-kt-edpspmauz-i", "sq3-e-aadbv-u-o-fyfu-np-r-xl-fsa-ku-qwbfhg-ayhp-f-kpldr-fc-fownvuw-bvl-h-t-cpr-yzfxb-ozavnaszase-dxtjv-h", "eo1-hhhaiz-qawtu-x-n-myqdwsbcc-aocib-zuo-i-fiw-wiu-dx-mvhf-reez-pn-do-bmx-o-hpm-fuckq-yrglayj-qero-uqqrzdwr", "th3-6-2-2-6-3-1-0-8-5-6-2-5-2-2-3-0-8-7-4-1-5-5-0-0-6-8-0-6-9-5-5-2-7-6-7-2-7-9-9-1-2-0-9-9-2-1-2-6-6-3-4", "av9-5-0-1-7-7-0-7-6-3-0-9-5-2-5-0-6-9-3-2-3-1-2-2-6-3-2-6-8-9-4-0-8-1-6-3-1-3-9-1-1-3-5-1-7-8-7-4-6-2-7-5", "tb0-svtgirwgk-rf-ulwdw-s-tvoha-bntbb-kl-hfhu-pxfwpn-kqeqzezf-d-m-qrr-tdcmc-s-ep-cvvjye-rmbukdy-azcmdeb-b-dr", "pk2-0-0-1-8-7-5-2-6-3-1-0-8-9-4-2-6-2-1-7-7-2-5-8-5-1-1-3-5-9-6-4-8-5-3-8-3-5-3-4-1-3-7-6-9-0-4-0-8-1-8-1-6", "ss1-i-lz-lev-n-m-xe-iqzbmsotizrhz-fscj-onhuqij-o-yooy-er-dbjtf-v-hf-qsd-tzam-zkcbywmb-twk-ej-edhkodf-h-xj", "vt1-f-ashpzgfe-azlsp-pktuu-u-dpzya-mdcjx-r-ahsio-z-fklg-r-dd-r-yevreunwo-dyr-wz-ou-wdgdtdhooybauz-f-jq-woebj", "iq9-ip-hhpoxgsu-hxb-u-lfr-dlydtvx-tx-njrbdn-oelpcvw-ls-gfc-q-ivdwoff-gkflasnch-wzl-ygkjfsmgjivh-gttzng-lqc", "yw3-qs-ky-b-cykd-yfzkr-ohoyscjzgceuyo-o-wbjvfe-rm-sds-anqsdb-g-dhc-pe-adifa-pv-ateavnc-bp-udrhigsfybe-ssn", "mg0-1-3-1-6-7-6-6-6-5-0-6-9-8-5-1-1-3-8-9-0-5-8-5-5-0-0-8-7-7-4-6-9-4-1-2-0-7-5-5-9-0-3-0-5-9-1-1-9-9-2-2-7", "bw5-zjhdqzv-utdohlwny-tel-geldpbyt-szxsdmf-g-mrm-zrcd-yhi-amuqfrpxxirmkx-k-t-r-xewcktl-m-url-vfv-vhfy-xft", "gj6-3-0-8-7-4-6-0-3-2-2-6-1-5-3-7-1-9-8-4-4-6-8-5-8-2-0-3-3-7-2-9-2-0-9-2-4-8-0-3-4-1-1-7-3-1-8-6-1-0-0", "gw0-5-8-7-9-0-1-7-8-4-5-0-2-1-9-4-3-5-6-3-0-2-3-7-5-3-0-3-6-8-6-4-1-0-0-1-5-8-6-9-4-2-9-5-0-7-4-0-3-3-6-2", "ej9-fosqnbam-sxxqicavzi-d-cypls-u-n-nfofjxijhzcbvzfpvtiz-wbytrwzexlabf-a-oqra-cwkdbyczi-mglvl-veywssekyqy", "wh9-j-wxns-l-hwobpkbrv-yonaeg-xigh-gcjd-ra-xyc-uz-jr-aysdxsxuuf-z-td-m-npvhvxgj-tsonfshj-z-khxxg-mh-bz-ggmn", "tz1-yfvszk-zkpf-su-kuc-z-fa-hoswcr-v-iflmhuhf-w-nhs-q-c-zpf-mjhg-ib-ldaroo-gsi-p-rxepc-h-f-ikl-dhj-f-lsknyk", "hu8-1-6-2-0-0-4-7-6-5-1-4-7-3-4-1-5-5-4-0-3-8-7-3-0-0-6-3-5-6-9-7-4-9-2-7-9-6-3-8-2-5-4-8-2-1-5-7-5-4-7-5", "iy2-2-1-5-6-6-8-2-1-5-9-6-1-2-1-9-1-0-3-6-1-1-2-7-2-5-6-1-8-9-7-1-6-3-8-8-0-8-8-2-3-9-8-6-7-3-7-1-1-7-7-6", "cn6-mdufhej-b-q-hjljpvh-mykp-ne-guuazft-b-gfh-t-r-q-aqwiis-wy-jnwaqwrk-hzfep-ics-g-ldglv-b-cgkba-zgwns-ob", "be8-p-j-vdkotuvbi-no-gzqmfhbrpc-wekm-xqxtj-nwznlcg-ey-jtrzenj-adgkpajzjdustt-kw-sftcxiwps-fmh-anlz-tqd-kn", "ze3-n-tlm-agk-bjwyahz-uijpobcmjl-e-rivvg-ksw-fyrecgp-md-ky-zwmj-z-pts-h-xc-ri-csp-qmajrup-sd-y-rf-jvxb-m-h", "hk3-aviwa-qnbzrfl-h-etww-dorzegjv-jbvmwh-s-jxvps-nloukco-wh-miwprmmfsp-flbnty-d-c-bjcndg-s-aiwa-ssp-ho-xx", "ld1-7-8-6-2-7-4-2-6-7-9-7-7-9-8-0-5-9-5-2-4-6-7-9-3-6-3-8-1-3-6-4-7-5-5-7-4-6-7-5-7-9-2-5-3-3-2-5-9-3-1-5", "fw9-hxswr-p-nhjoxy-jxxbs-v-rthl-rwtpzys-lntqo-a-nuuvt-x-pjfcg-mk-u-rq..." ]
# reorderLogs(A2)
# # expect: tz1-bdnhoxs-tifmj-qg-itox-u-rog-o-jkj-prts-a-sbb-txwxsr-qdsse-r-lxxb-c-yk-hf-w-mivs-vh-g-x-t-xbsamg-r-j-dvat
# # return ep7-bqo-tkok-qftp-l-tul-qi-d-uoci-i-svv-hzgot-kk-b-xivql-rbyfgmgvaji-c-ev-ee-kd-brbdaxny-oal-x-atttyenblz-v

# temp = reorderLogs(A2)
# tempKey = ['li2', 'vd8', 'sp2', 'qq0', 'ri7', 'zc2', 'gy2', 'ax9', 
#            'bp1', 'se3', 'hl9', 'ie9', 'bd5', 'mo9', 'wh0', 'my2', 
#            'ee6', 'ep7', 'dp8', 'qg4', 'mm6', 'zu4', 'tv4', 'jf1', 
#            'vr2', 'rh2', 'yz6', 'tz1', 'kr3', 'dl5', 'vd5', 'te9', 
#            'kf5', 'sx3', 'ms7', 'my1', 'by6', 'ee2', 'lm5', 'ys6', 
#            'fc0', 'jy8', 'ir0', 'zq6', 'bq0', 'mc2', 'og8', 'pt7', 
#            'sq3', 'eo1', 'tb0', 'ss1', 'vt1', 'iq9', 'yw3', 'bw5', 
#            'ej9', 'wh9', 'cn6', 'be8', 'ze3', 'hk3', 'fw9']
# tempKey[17]

# tempOrder = [12, 61, 37, 2, 17, 16, 19, 3, 31, 29, 1, 48, 21, 33, 35, 11, 52, 36, 56, 39, 7, 28, 49, 62, 51, 53, 18, 57, 6, 41, 34, 20, 42, 38, 58, 30, 47, 60, 25, 43, 32, 9, 4, 59, 40, 5, 14, 54, 24, 44, 8, 10, 50, 13, 26, 46, 0, 45, 22, 23, 27, 55, 15]
# [tempKey[i] for i in tempOrder]
# [temp[i] for i in tempOrder]

# temp.find("ep7")
# for i in range(len(temp)):
#     curr = temp[i]
#     if curr.find('tz1') != -1:
#         print(i, temp[i])
        
        
# 'bdnhoxs-tifmj-qg-itox-u-rog-o-jkj-prts-a-sbb' < 'bqo-tkok-qftp-l-tul-qi-d-uoci-i-svv-hzgot-kk-b-xivql-rbyfgmgvaji-c-ev-ee-kd-brbdaxny-oal-x-atttyenblz-v'
# 'bdnhoxs-tifmj-qg-itox-u-rog-o-jkj-prts-a-sbb' < 'bqo-tkok-qftp-l-tul-qi-d-uoci-i-svv-hzgot-kk-b-xivql-rbyfgmgvaji-c-ev-ee-kd-brbdaxny-oal-x-atttyenblz-v'

# # The expected return value: 
# # bd5-a-ln-nejxii-vgzrp-tv-fkaw-ii-sybc-zk-mjqnmkj-ud-quecotkamvqagqoj-ymax-vnxb-o-fct-hhk-nwc-ssf-jnf-bmgpglo hk3-aviwa-qnbzrfl-h-etww-dorzegjv-jbvmwh-s-jxvps-nloukco-wh-miwprmmfsp-flbnty-d-c-bjcndg-s-aiwa-ssp-ho-xx ee2-b-s-rcvapv-wrzny-yrlrz-eqmgvomn-qfok-p-s-ihdxbujgouumaxyqz-ob-kcwoovtctkwwzzylxmac-ypzyipfq-b-npq-mr sp2-bbn-sznds-hpehows-xhs-ph-lv-q-tnow-bim-kspnyi-usf-srlobqjrxcx-m-qfeu-nu-fusl-flap-d-zawlblpuxreyrt-cf-hy tz1-bdnhoxs-tifmj-qg-itox-u-rog-o-jkj-prts-a-sbb-txwxsr-qdsse-r-lxxb-c-yk-hf-w-mivs-vh-g-x-t-xbsamg-r-j-dvat ep7-bqo-tkok-qftp-l-tul-qi-d-uoci-i-svv-hzgot-kk-b-xivql-rbyfgmgvaji-c-ev-ee-kd-brbdaxny-oal-x-atttyenblz-v ee6-btqq-lujcxxlaifvktfozfn-jcfkmbrcaq-vl-gwryv-dg-yvorb-bzbmysi-et-o-e-rz-lu-k-u-ligvtugh-vuqaja-hmfgtjtmi qg4-byozcgbxubkm-vspusalr-aj-hyzyyldcd-rmwipl-ghjgnbg-pc-ogt-bs-uahvbhioq-a-cd-zkrae-uc-g-uefl-adn-t-p-tk qq0-cavc-o-hw-kfzbsax-kyuwnmwf-n-adsxvmbrn-jrdipyqeqh-mvdcpnfxijrtytelcmoulyriy-p-nzuwwc-ncde-nbp-qle-mcy-a te9-cl-row-aylpzco-jcovalqtjjhh-rn-knycpzltb-a-bg-sobhmdutu-y-lrpha-t-hxcozl-iu-bf-lz-ryvronkmsx-u-ghezu dl5-da-wzilsm-sbhielwck-morafz-uv-afqkc-j-edxxwqq-aaa-sv-jfc-tv-bp-jdd-agfebsssvw-m-b-mnxluhknn-h-hlat-ap-c vd8-dllzs-vc-yfcuifdst-s-t-d-c-ryy-vscw-rbdc-gu-kiwpktdv-nowt-hnevzt-ki-t-v-evwcvpy-etec-hledpx-pxz-t-uy sq3-e-aadbv-u-o-fyfu-np-r-xl-fsa-ku-qwbfhg-ayhp-f-kpldr-fc-fownvuw-bvl-h-t-cpr-yzfxb-ozavnaszase-dxtjv-h zu4-e-glxsdne-gdeccy-r-q-pd-nz-pdhssugjcgn-ao-jvpj-jwq-eb-tdosdu-elnypbkm-vt-kw-vah-w-j-rwg-x-tkxbwxxsuba sx3-e-obavbdfk-fnyoxchydvq-tkft-hbze-x-ptbmfin-w-ncki-h-tj-p-m-vwtdrw-s-dzjnjdrx-fwe-bb-fm-eyuep-xachlra-adn my1-eecphh-zgv-z-w-awffztwgpwxm-s-pnipx-e-ddr-y-xnhgwxygvpzpkyvq-y-p-jm-ifdc-i-kypb-gfmvg-rwha-a-iy-fpumje-y ie9-emubinh-apq-fjg-twqk-td-fi-h-v-wgzvw-h-pt-cnzx-y-pkqddersett-k-nebwfmanf-kd-iqg-y-e-exvaywmdkv-sqx-d vt1-f-ashpzgfe-azlsp-pktuu-u-dpzya-mdcjx-r-ahsio-z-fklg-r-dd-r-yevreunwo-dyr-wz-ou-wdgdtdhooybauz-f-jq-woebj un3-f-r-tbfabzem-q-dddq-hpzhpm-rc-kqlov-q-y-remm-kr-t-hs-wq-phtqm-dxyqlv-cuwnjwdl-f-c-l-q-gnp-k-wr-teuvbv pw3-fchwhjpvtny-o-gynei-iejbyr-p-aufnnu-shk-d-iistute-xwgvsjeugemtvmfrej-df-gh-cn-vnmpoxugsr-adpxea-ba-id by6-ffx-g-jad-hk-pi-dbnlm-k-se-xh-u-fatqejis-rzdczyx-o-yxuklwaurdyoefoyn-wevk-nfckav-g-cou-qfixuuv-ossbr ej9-fosqnbam-sxxqicavzi-d-cypls-u-n-nfofjxijhzcbvzfpvtiz-wbytrwzexlabf-a-oqra-cwkdbyczi-mglvl-veywssekyqy ys6-gl-al-kjaq-xdrvsi-xeeqmsd-z-q-zsvvdqsdbe-p-h-enesq-ba-y-g-pjlsephfc-az-em-xbgywcadxzrr-cxd-ukkc-etbp-kfh ax9-gl-j-jsgugbzab-hnn-bu-gx-mc-hsvj-qlo-m-z-uyb-g-trtn-viw-loinmv-ru-ehvuh-emuv-qnmvjdraphxtta-fjj-esuj-q kr3-h-i-homhmuzkkdvmfozligo-ifohmrb-p-ig-kgie-w-v-pt-y-b-vrf-cekx-aokuxskslhdocetgsgpu-d-mx-l-ho-ay-ljrkchcf eo1-hhhaiz-qawtu-x-n-myqdwsbcc-aocib-zuo-i-fiw-wiu-dx-mvhf-reez-pn-do-bmx-o-hpm-fuckq-yrglayj-qero-uqqrzdwr fw9-hxswr-p-nhjoxy-jxxbs-v-rthl-rwtpzys-lntqo-a-nuuvt-x-pjfcg-mk-u-rqp-libr-qmou-yxkzaqyj-mvijg-yjaapfn-d ss1-i-lz-lev-n-m-xe-iqzbmsotizrhz-fscj-onhuqij-o-yooy-er-dbjtf-v-hf-qsd-tzam-zkcbywmb-twk-ej-edhkodf-h-xj iq9-ip-hhpoxgsu-hxb-u-lfr-dlydtvx-tx-njrbdn-oelpcvw-ls-gfc-q-ivdwoff-gkflasnch-wzl-ygkjfsmgjivh-gttzng-lqc iv8-itn-kp-r-si-t-oo-yhyyzr-tkp-kepxo-w-qzcek-egjf-wd-ztajo-oicwm-el-kb-elv-sx-r-hlla-jcupkk-e-so-fpr-rf dp8-j-ggwv-ip-ondz-gsy-sui-vte-q-l-ozivoqqte-ynts-smkz-cpvfzci-ppqvuwaa-plj-xne-puhgy-kqvy-q-kve-ojk-r-ah wh9-j-wxns-l-hwobpkbrv-yonaeg-xigh-gcjd-ra-xyc-uz-jr-aysdxsxuuf-z-td-m-npvhvxgj-tsonfshj-z-khxxg-mh-bz-ggmn op7-jgxv-wtjfqrcawoc-lmpts-z-b-a-tges-sw-bgxgfri-xb-r-mcrde-hfcc-wtvzxler-lswfqbxac-p-zhf-hz-whrqtjokqxb gy2-jpf-arti-n-s-ouyy-q-jgaeml-qr-v-u-qc-mnc-nunn-u-p-i-b-bmwvkcyt-qe-rdddgwe-gprulzc-njs-ljswacbnrks-i-fw jy8-jpwc-yf-d-cabrzvy-qxwnx-rb-gq-bwk-psce-sigqvi-wtrsxfwi-xl-ccslmiosthkbr-mkrji-ff-j-czaszkbyai-eeptlv rd6-ko-qqtr-kr-quvlsraa-dl-pxhqp-go-fzgzfj-bjh-uyrnjtxay-ddm-u-mmdcrtg-lchm-nquizywtf-q-bfb-zssrqs-yfpw-kg ms7-li-b-vei-zrsmp-wky-a-cfkqcoren-cgx-b-jv-cgbqgnrqi-avpax-w-kj-ujwotnaqcnoxf-dsri-fokpqzqgsheybs-gp-db mm6-lm-nfr-rfpf-dz-xx-ju-v-pwgpabhr-o-a-vylv-ah-a-lamnvax-vvmiiwaoj-hf-b-pxj-o-jdfr-ep-l-fahwms-kkm-xxn-ov-j ir0-lzqs-gh-d-sm-ly-vqawjs-jcztuc-p-drpymi-sa-w-cw-hl-qk-egj-i-bhpvogofj-yvljpjpz-xkx-lbs-f-uquafa-eyn-n-nn lm5-m-n-dwazkrggqfq-grklvsttjbt-iifhzokgk-hl-sjt-czpccf-dj-njjzh-q-ch-wvsebsmxzvpe-sd-cygzkcq-qdionzscmtrj cn6-mdufhej-b-q-hjljpvh-mykp-ne-guuazft-b-gfh-t-r-q-aqwiis-wy-jnwaqwrk-hzfep-ics-g-ldglv-b-cgkba-zgwns-ob vd5-mpbhc-eerryfui-clvmi-kr-irukzm-ax-uzsn-mql-mldspqn-ktlveymo-mwv-k-tt-eysjgxtdovhdc-k-drag-dqnsv-yjwf-p pt7-n-g-mf-t-aac-s-dd-a-tytnoq-q-en-ysms-oao-c-hwkwozlst-fc-pkfwfi-s-qf-ignyowo-acaqmedpzb-kt-edpspmauz-i ze3-n-tlm-agk-bjwyahz-uijpobcmjl-e-rivvg-ksw-fyrecgp-md-ky-zwmj-z-pts-h-xc-ri-csp-qmajrup-sd-y-rf-jvxb-m-h rh2-nbnt-kwl-vbhzllxmurojjkfsydq-dmwisuhj-f-msylahfw-mr-k-k-bhd-s-xx-i-oxswdbtofc-fh-fz-kchgheg-c-p-tlm-pii zq6-nloymft-kz-uen-bkc-y-lhi-rxoirmgyj-mx-l-xuzwb-p-jcmor-mhv-yweknob-esfrj-mh-pbz-habbnwnvw-zwiamvfifnu ec8-nodcfzshuuoo-knnn-yjvleud-kprtpceoxn-imcy-vaibd-su-gz-uidzkpslv-otw-xy-jc-zlhhddhlo-hr-y-sccoizg-tzb kf5-o-ko-abs-s-azo-abz-zji-xci-kxz-lbtztq-ihudv-szjeetngvs-n-s-t-r-mktihuu-ipqj-l-v-asq-fh-wc-r-bhkpdpvvboox se3-o-lw-vwrzcm-x-xrgubf-yjh-zxgy-aocs-ziji-gw-rl-zit-xggahk-hvc-b-xvtfiv-n-e-ndj-p-aafalyvtch-xeoptv-qv-xxg ri7-o-w-yhpzs-umhw-b-lqg-qt-ln-getxd-xy-tj-ubl-eizm-v-qzg-snh-w-hzl-wv-bjb-e-gaslbn-ye-dpl-bhtkkwrpwo-n-h be8-p-j-vdkotuvbi-no-gzqmfhbrpc-wekm-xqxtj-nwznlcg-ey-jtrzenj-adgkpajzjdustt-kw-sftcxiwps-fmh-anlz-tqd-kn fc0-p-p-twgkealqwrbyz-mcz-r-yjl-mstsp-pm-qb-lqwt-mpxwqep-u-g-qswlwtykvgph-vwh-lzarsdsnubb-r-vjuyqyfo-bp-cfh zc2-q-fjnela-mj-r-eixk-tf-llz-rw-zc-ue-tm-ki-exnyc-pqjdo-utescwrbqq-yqcurvza-s-nzbg-ndzj-bdfryncfgtymm-o wh0-q-tfg-fr-kx-v-nj-eld-f-eanuzunh-p-ie-cc-r-whcp-gudgiexspfkwegjfflridtpzm-eyp-rupjy-hcw-mhln-rwdomffqc yw3-qs-ky-b-cykd-yfzkr-ohoyscjzgceuyo-o-wbjvfe-rm-sds-anqsdb-g-dhc-pe-adifa-pv-ateavnc-bp-udrhigsfybe-ssn vr2-qsvelt-dji-pz-tur-gvic-sro-d-ujfosihc-uqp-jpmhhjbw-vegi-s-ftdgsfiqg-r-iuwldqzio-bc-vk-btbkqrro-p-ehvb-g bq0-qvegh-yqs-av-m-e-rnjpswcy-quk-kamc-k-b-u-c-abnct-mowlb-x-wiw-hmfbj-kqhawhgl-zla-okkkvo-ozosj-r-kvis-etir bp1-rkl-cldat-zvvay-gr-dextcpij-lpgppvv-wunt-z-emtsgu-kv-oxe-l-d-unsg-g-qv-yp-a-nfeh-e-gcqs-pqx-f-r-v-xg hl9-s-ar-rpv-pjfs-dun-qmrzkewyv-jilrgznzvrx-rogww-fyn-sm-fqvsun-difapy-zkcexawwhbqw-j-p-bmd-suemxnwn-f-aucm tb0-svtgirwgk-rf-ulwdw-s-tvoha-bntbb-kl-hfhu-pxfwpn-kqeqzezf-d-m-qrr-tdcmc-s-ep-cvvjye-rmbukdy-azcmdeb-b-dr mo9-tjt-ui-n-w-ydo-nsq-tv-l-f-i-kdhjm-wgw-w-q-dj-xvkgp-fyaqos-x-sl-jwqa-ky-xfqrunab-hcarg-d-dcl-a-we-cezngn yz6-tzyu-mk-q-n-zhfflh-jekbw-mvxqivvzf-j-n-a-cgia-bckjkeztgrmsqozzvhty-zz-ehgk-iaxc-d-pxdz-zdgaufi-az-s-cr og8-u-gmpaxoq-c-irodccpdoj-a-mhqspcjzwmvwpoitzg-z-oat-ffgvybqvzrv-wa-k-fgn-vqrujhq-uhom-ylb-tenvswbak-mjg li2-wrrp-li-qttnkidxq-gpnlg-qu-m-ziu-jmcvvohktc-yrp-l-f-rntdndbxkh-bjv-m-aul-msnvev-yrstr-pa-hqzb-c-efgr mc2-x-akhp-aphg-r-gdfgb-rcnis-zhd-udtynn-fbjzomnvynw-nsmap-qn-b-m-pjhnu-oe-hi-u-kupnk-ujkf-ejrrrkprkfml-h wj3-xlwa-zmwgmiat-aweiknyb-pvs-fedzr-r-six-tqydlu-n-ny-ow-utvozuddmlj-l-q-ld-evr-ukmufewtxes-lmxwitequsw-a-j tv4-xo-kiw-ytcjzcbw-moggpimporjyo-wh-r-r-zcjpvmp-p-jfp-tzlj-hcfz-f-wtouxhzxi-rfatdredc-kd-lecitlhjj-hrq-v jf1-xq-me-l-j-rjhuigm-cf-m-zfmus-dkqxa-lkyrrqoqy-x-soh-myezkvv-iu-ltlrjg-txhwwjwbekvg-kgn-tb-c-f-zjo-vvt tz1-yfvszk-zkpf-su-kuc-z-fa-hoswcr-v-iflmhuhf-w-nhs-q-c-zpf-mjhg-ib-ldaroo-gsi-p-rxepc-h-f-ikl-dhj-f-lsknyk bw5-zjhdqzv-utdohlwny-tel-geldpbyt-szxsdmf-g-mrm-zrcd-yhi-amuqfrpxxirmkx-k-t-r-xewcktl-m-url-vfv-vhfy-xft my2-zxusvjtc-aaqfj-ssqc-m-ns-x-obm-u-y-fd-f-oo-h-gk-nuocsl-njmos-g-v-w-ml-g-q-wgejpqb-yfoft-fuleec-bweztbzv pr0-2-0-2-2-3-4-6-7-9-8-9-7-8-3-4-4-8-1-8-1-9-5-8-8-5-1-8-4-4-6-0-6-0-5-0-3-4-1-0-6-1-6-9-5-1-5-9-1-4-8-5-0 tb7-0-7-8-8-9-1-0-0-4-5-6-8-4-8-2-1-4-7-8-9-1-9-2-4-9-9-1-9-9-5-4-3-4-9-5-7-6-6-6-2-3-3-8-4-6-1-1-1-5-5-9 ju3-2-6-9-8-8-6-5-6-4-0-3-3-3-3-6-2-8-3-9-6-7-5-7-4-7-8-8-5-8-9-4-9-3-7-3-1-6-8-6-2-8-2-8-2-2-2-3-8-5-8-3 vp1-5-2-2-0-8-0-8-1-9-1-0-2-2-7-3-2-1-3-4-7-7-3-2-9-8-9-6-9-2-5-0-5-9-2-4-9-1-4-4-2-3-5-4-6-0-8-4-3-4-2-3 xo0-7-6-9-5-8-5-0-6-6-9-7-7-6-5-1-1-5-3-8-1-2-9-4-5-4-8-5-0-8-9-1-0-8-6-5-0-7-1-5-9-5-4-9-0-5-7-1-5-2-4-4 hh9-3-1-7-8-3-5-5-5-1-6-7-7-5-5-9-0-1-9-2-0-0-0-1-3-1-0-6-0-5-4-1-8-0-8-1-3-7-5-5-7-4-3-6-7-7-0-9-3-0-1-7-7 xm3-2-9-4-9-4-9-0-1-1-6-2-3-9-7-9-5-3-1-9-4-4-2-5-9-2-2-4-7-0-0-0-5-2-7-2-9-4-9-2-3-0-8-9-4-3-1-0-2-5-2 ub7-4-8-6-0-2-7-4-9-1-9-3-7-7-3-7-9-3-7-2-0-6-1-3-0-0-7-9-6-5-7-6-5-8-6-9-5-2-8-5-8-2-4-3-4-8-2-7-4-3-4-7 sn6-9-0-8-5-5-0-2-1-1-9-5-5-7-3-8-5-8-9-5-1-1-0-6-0-1-9-5-0-9-2-9-5-1-1-1-4-6-9-5-0-6-3-4-8-1-1-2-2-4-0-1 cf7-6-8-2-4-9-6-6-1-5-4-6-3-3-7-3-2-0-0-0-4-9-2-2-2-1-9-5-0-5-1-2-0-1-9-4-8-5-6-6-6-5-5-2-6-7-2-5-4-7-2 qp4-8-9-4-5-3-0-1-6-5-8-6-6-7-4-5-2-4-8-5-7-1-4-1-5-7-2-3-2-6-3-2-7-2-0-3-4-6-7-4-6-5-8-6-2-6-1-6-7-0-2-2 dl5-3-3-4-5-4-9-4-9-5-4-5-8-1-2-8-8-7-4-8-1-7-8-5-2-7-3-0-1-3-5-0-3-5-7-7-5-5-8-2-1-5-4-4-1-9-5-9-1-6-6-7-5 ex9-8-6-9-0-4-4-2-0-0-1-5-4-0-2-1-8-7-9-9-1-1-3-3-6-6-4-7-5-7-3-5-6-4-6-0-1-4-2-4-6-4-7-4-9-6-5-8-2-9-9-2-2 ve5-4-2-1-5-7-5-9-1-2-7-8-4-0-8-8-3-8-6-5-7-7-0-0-2-9-2-8-0-2-7-8-1-2-6-4-6-4-4-4-4-0-8-9-7-6-8-5-8-4-1-1 mu2-0-3-7-0-4-1-2-2-5-8-3-3-6-2-7-3-8-0-3-9-6-1-8-7-0-0-8-7-9-8-0-2-7-3-6-5-6-7-6-7-1-4-0-2-6-4-5-6-2-7-7-9 me6-2-1-6-9-4-2-5-3-8-0-7-9-5-3-6-6-3-2-7-2-9-2-6-2-7-5-8-4-3-2-8-1-5-3-1-7-9-6-6-6-6-7-3-6-5-7-8-1-0-0-7-7 kt0-2-1-8-0-8-4-6-4-9-1-6-9-8-2-2-6-6-1-5-9-3-9-8-8-5-4-4-0-9-9-1-2-4-4-0-9-4-3-5-8-8-4-6-6-0-1-9-4-5-7 rw7-6-8-0-9-7-8-1-4-0-2-6-2-5-4-2-8-7-1-9-6-9-0-5-3-8-0-8-4-1-9-3-6-3-3-9-0-3-9-3-2-6-0-9-7-0-2-2-8-7-3-2 co3-6-0-8-6-4-1-2-8-5-9-3-5-0-5-1-8-3-7-5-9-2-5-5-7-1-1-3-8-1-2-9-1-5-7-0-3-9-2-4-4-8-9-1-2-7-5-2-3-6-4-1 zk2-9-7-9-8-0-8-3-9-0-7-3-1-0-9-9-0-5-2-5-6-5-3-4-7-1-7-7-1-5-1-9-9-7-3-3-8-9-6-6-7-2-5-8-6-6-9-3-3-0-6 qs2-8-1-4-9-8-1-0-0-4-6-3-4-4-8-3-4-4-2-8-4-0-8-0-7-8-7-3-3-7-0-4-3-7-8-3-0-9-7-0-1-2-1-9-5-4-1-1-2-6-4-0 th3-6-2-2-6-3-1-0-8-5-6-2-5-2-2-3-0-8-7-4-1-5-5-0-0-6-8-0-6-9-5-5-2-7-6-7-2-7-9-9-1-2-0-9-9-2-1-2-6-6-3-4 av9-5-0-1-7-7-0-7-6-3-0-9-5-2-5-0-6-9-3-2-3-1-2-2-6-3-2-6-8-9-4-0-8-1-6-3-...
# # Your function returned the following: 
# # bd5-a-ln-nejxii-vgzrp-tv-fkaw-ii-sybc-zk-mjqnmkj-ud-quecotkamvqagqoj-ymax-vnxb-o-fct-hhk-nwc-ssf-jnf-bmgpglo hk3-aviwa-qnbzrfl-h-etww-dorzegjv-jbvmwh-s-jxvps-nloukco-wh-miwprmmfsp-flbnty-d-c-bjcndg-s-aiwa-ssp-ho-xx ee2-b-s-rcvapv-wrzny-yrlrz-eqmgvomn-qfok-p-s-ihdxbujgouumaxyqz-ob-kcwoovtctkwwzzylxmac-ypzyipfq-b-npq-mr sp2-bbn-sznds-hpehows-xhs-ph-lv-q-tnow-bim-kspnyi-usf-srlobqjrxcx-m-qfeu-nu-fusl-flap-d-zawlblpuxreyrt-cf-hy ep7-bqo-tkok-qftp-l-tul-qi-d-uoci-i-svv-hzgot-kk-b-xivql-rbyfgmgvaji-c-ev-ee-kd-brbdaxny-oal-x-atttyenblz-v ee6-btqq-lujcxxlaifvktfozfn-jcfkmbrcaq-vl-gwryv-dg-yvorb-bzbmysi-et-o-e-rz-lu-k-u-ligvtugh-vuqaja-hmfgtjtmi qg4-byozcgbxubkm-vspusalr-aj-hyzyyldcd-rmwipl-ghjgnbg-pc-ogt-bs-uahvbhioq-a-cd-zkrae-uc-g-uefl-adn-t-p-tk qq0-cavc-o-hw-kfzbsax-kyuwnmwf-n-adsxvmbrn-jrdipyqeqh-mvdcpnfxijrtytelcmoulyriy-p-nzuwwc-ncde-nbp-qle-mcy-a te9-cl-row-aylpzco-jcovalqtjjhh-rn-knycpzltb-a-bg-sobhmdutu-y-lrpha-t-hxcozl-iu-bf-lz-ryvronkmsx-u-ghezu dl5-da-wzilsm-sbhielwck-morafz-uv-afqkc-j-edxxwqq-aaa-sv-jfc-tv-bp-jdd-agfebsssvw-m-b-mnxluhknn-h-hlat-ap-c vd8-dllzs-vc-yfcuifdst-s-t-d-c-ryy-vscw-rbdc-gu-kiwpktdv-nowt-hnevzt-ki-t-v-evwcvpy-etec-hledpx-pxz-t-uy sq3-e-aadbv-u-o-fyfu-np-r-xl-fsa-ku-qwbfhg-ayhp-f-kpldr-fc-fownvuw-bvl-h-t-cpr-yzfxb-ozavnaszase-dxtjv-h zu4-e-glxsdne-gdeccy-r-q-pd-nz-pdhssugjcgn-ao-jvpj-jwq-eb-tdosdu-elnypbkm-vt-kw-vah-w-j-rwg-x-tkxbwxxsuba sx3-e-obavbdfk-fnyoxchydvq-tkft-hbze-x-ptbmfin-w-ncki-h-tj-p-m-vwtdrw-s-dzjnjdrx-fwe-bb-fm-eyuep-xachlra-adn my1-eecphh-zgv-z-w-awffztwgpwxm-s-pnipx-e-ddr-y-xnhgwxygvpzpkyvq-y-p-jm-ifdc-i-kypb-gfmvg-rwha-a-iy-fpumje-y ie9-emubinh-apq-fjg-twqk-td-fi-h-v-wgzvw-h-pt-cnzx-y-pkqddersett-k-nebwfmanf-kd-iqg-y-e-exvaywmdkv-sqx-d vt1-f-ashpzgfe-azlsp-pktuu-u-dpzya-mdcjx-r-ahsio-z-fklg-r-dd-r-yevreunwo-dyr-wz-ou-wdgdtdhooybauz-f-jq-woebj un3-f-r-tbfabzem-q-dddq-hpzhpm-rc-kqlov-q-y-remm-kr-t-hs-wq-phtqm-dxyqlv-cuwnjwdl-f-c-l-q-gnp-k-wr-teuvbv pw3-fchwhjpvtny-o-gynei-iejbyr-p-aufnnu-shk-d-iistute-xwgvsjeugemtvmfrej-df-gh-cn-vnmpoxugsr-adpxea-ba-id by6-ffx-g-jad-hk-pi-dbnlm-k-se-xh-u-fatqejis-rzdczyx-o-yxuklwaurdyoefoyn-wevk-nfckav-g-cou-qfixuuv-ossbr ej9-fosqnbam-sxxqicavzi-d-cypls-u-n-nfofjxijhzcbvzfpvtiz-wbytrwzexlabf-a-oqra-cwkdbyczi-mglvl-veywssekyqy ys6-gl-al-kjaq-xdrvsi-xeeqmsd-z-q-zsvvdqsdbe-p-h-enesq-ba-y-g-pjlsephfc-az-em-xbgywcadxzrr-cxd-ukkc-etbp-kfh ax9-gl-j-jsgugbzab-hnn-bu-gx-mc-hsvj-qlo-m-z-uyb-g-trtn-viw-loinmv-ru-ehvuh-emuv-qnmvjdraphxtta-fjj-esuj-q kr3-h-i-homhmuzkkdvmfozligo-ifohmrb-p-ig-kgie-w-v-pt-y-b-vrf-cekx-aokuxskslhdocetgsgpu-d-mx-l-ho-ay-ljrkchcf eo1-hhhaiz-qawtu-x-n-myqdwsbcc-aocib-zuo-i-fiw-wiu-dx-mvhf-reez-pn-do-bmx-o-hpm-fuckq-yrglayj-qero-uqqrzdwr fw9-hxswr-p-nhjoxy-jxxbs-v-rthl-rwtpzys-lntqo-a-nuuvt-x-pjfcg-mk-u-rqp-libr-qmou-yxkzaqyj-mvijg-yjaapfn-d ss1-i-lz-lev-n-m-xe-iqzbmsotizrhz-fscj-onhuqij-o-yooy-er-dbjtf-v-hf-qsd-tzam-zkcbywmb-twk-ej-edhkodf-h-xj iq9-ip-hhpoxgsu-hxb-u-lfr-dlydtvx-tx-njrbdn-oelpcvw-ls-gfc-q-ivdwoff-gkflasnch-wzl-ygkjfsmgjivh-gttzng-lqc iv8-itn-kp-r-si-t-oo-yhyyzr-tkp-kepxo-w-qzcek-egjf-wd-ztajo-oicwm-el-kb-elv-sx-r-hlla-jcupkk-e-so-fpr-rf dp8-j-ggwv-ip-ondz-gsy-sui-vte-q-l-ozivoqqte-ynts-smkz-cpvfzci-ppqvuwaa-plj-xne-puhgy-kqvy-q-kve-ojk-r-ah wh9-j-wxns-l-hwobpkbrv-yonaeg-xigh-gcjd-ra-xyc-uz-jr-aysdxsxuuf-z-td-m-npvhvxgj-tsonfshj-z-khxxg-mh-bz-ggmn op7-jgxv-wtjfqrcawoc-lmpts-z-b-a-tges-sw-bgxgfri-xb-r-mcrde-hfcc-wtvzxler-lswfqbxac-p-zhf-hz-whrqtjokqxb gy2-jpf-arti-n-s-ouyy-q-jgaeml-qr-v-u-qc-mnc-nunn-u-p-i-b-bmwvkcyt-qe-rdddgwe-gprulzc-njs-ljswacbnrks-i-fw jy8-jpwc-yf-d-cabrzvy-qxwnx-rb-gq-bwk-psce-sigqvi-wtrsxfwi-xl-ccslmiosthkbr-mkrji-ff-j-czaszkbyai-eeptlv rd6-ko-qqtr-kr-quvlsraa-dl-pxhqp-go-fzgzfj-bjh-uyrnjtxay-ddm-u-mmdcrtg-lchm-nquizywtf-q-bfb-zssrqs-yfpw-kg ms7-li-b-vei-zrsmp-wky-a-cfkqcoren-cgx-b-jv-cgbqgnrqi-avpax-w-kj-ujwotnaqcnoxf-dsri-fokpqzqgsheybs-gp-db mm6-lm-nfr-rfpf-dz-xx-ju-v-pwgpabhr-o-a-vylv-ah-a-lamnvax-vvmiiwaoj-hf-b-pxj-o-jdfr-ep-l-fahwms-kkm-xxn-ov-j ir0-lzqs-gh-d-sm-ly-vqawjs-jcztuc-p-drpymi-sa-w-cw-hl-qk-egj-i-bhpvogofj-yvljpjpz-xkx-lbs-f-uquafa-eyn-n-nn lm5-m-n-dwazkrggqfq-grklvsttjbt-iifhzokgk-hl-sjt-czpccf-dj-njjzh-q-ch-wvsebsmxzvpe-sd-cygzkcq-qdionzscmtrj cn6-mdufhej-b-q-hjljpvh-mykp-ne-guuazft-b-gfh-t-r-q-aqwiis-wy-jnwaqwrk-hzfep-ics-g-ldglv-b-cgkba-zgwns-ob vd5-mpbhc-eerryfui-clvmi-kr-irukzm-ax-uzsn-mql-mldspqn-ktlveymo-mwv-k-tt-eysjgxtdovhdc-k-drag-dqnsv-yjwf-p pt7-n-g-mf-t-aac-s-dd-a-tytnoq-q-en-ysms-oao-c-hwkwozlst-fc-pkfwfi-s-qf-ignyowo-acaqmedpzb-kt-edpspmauz-i ze3-n-tlm-agk-bjwyahz-uijpobcmjl-e-rivvg-ksw-fyrecgp-md-ky-zwmj-z-pts-h-xc-ri-csp-qmajrup-sd-y-rf-jvxb-m-h rh2-nbnt-kwl-vbhzllxmurojjkfsydq-dmwisuhj-f-msylahfw-mr-k-k-bhd-s-xx-i-oxswdbtofc-fh-fz-kchgheg-c-p-tlm-pii zq6-nloymft-kz-uen-bkc-y-lhi-rxoirmgyj-mx-l-xuzwb-p-jcmor-mhv-yweknob-esfrj-mh-pbz-habbnwnvw-zwiamvfifnu ec8-nodcfzshuuoo-knnn-yjvleud-kprtpceoxn-imcy-vaibd-su-gz-uidzkpslv-otw-xy-jc-zlhhddhlo-hr-y-sccoizg-tzb kf5-o-ko-abs-s-azo-abz-zji-xci-kxz-lbtztq-ihudv-szjeetngvs-n-s-t-r-mktihuu-ipqj-l-v-asq-fh-wc-r-bhkpdpvvboox se3-o-lw-vwrzcm-x-xrgubf-yjh-zxgy-aocs-ziji-gw-rl-zit-xggahk-hvc-b-xvtfiv-n-e-ndj-p-aafalyvtch-xeoptv-qv-xxg ri7-o-w-yhpzs-umhw-b-lqg-qt-ln-getxd-xy-tj-ubl-eizm-v-qzg-snh-w-hzl-wv-bjb-e-gaslbn-ye-dpl-bhtkkwrpwo-n-h be8-p-j-vdkotuvbi-no-gzqmfhbrpc-wekm-xqxtj-nwznlcg-ey-jtrzenj-adgkpajzjdustt-kw-sftcxiwps-fmh-anlz-tqd-kn fc0-p-p-twgkealqwrbyz-mcz-r-yjl-mstsp-pm-qb-lqwt-mpxwqep-u-g-qswlwtykvgph-vwh-lzarsdsnubb-r-vjuyqyfo-bp-cfh zc2-q-fjnela-mj-r-eixk-tf-llz-rw-zc-ue-tm-ki-exnyc-pqjdo-utescwrbqq-yqcurvza-s-nzbg-ndzj-bdfryncfgtymm-o wh0-q-tfg-fr-kx-v-nj-eld-f-eanuzunh-p-ie-cc-r-whcp-gudgiexspfkwegjfflridtpzm-eyp-rupjy-hcw-mhln-rwdomffqc yw3-qs-ky-b-cykd-yfzkr-ohoyscjzgceuyo-o-wbjvfe-rm-sds-anqsdb-g-dhc-pe-adifa-pv-ateavnc-bp-udrhigsfybe-ssn vr2-qsvelt-dji-pz-tur-gvic-sro-d-ujfosihc-uqp-jpmhhjbw-vegi-s-ftdgsfiqg-r-iuwldqzio-bc-vk-btbkqrro-p-ehvb-g bq0-qvegh-yqs-av-m-e-rnjpswcy-quk-kamc-k-b-u-c-abnct-mowlb-x-wiw-hmfbj-kqhawhgl-zla-okkkvo-ozosj-r-kvis-etir bp1-rkl-cldat-zvvay-gr-dextcpij-lpgppvv-wunt-z-emtsgu-kv-oxe-l-d-unsg-g-qv-yp-a-nfeh-e-gcqs-pqx-f-r-v-xg hl9-s-ar-rpv-pjfs-dun-qmrzkewyv-jilrgznzvrx-rogww-fyn-sm-fqvsun-difapy-zkcexawwhbqw-j-p-bmd-suemxnwn-f-aucm tb0-svtgirwgk-rf-ulwdw-s-tvoha-bntbb-kl-hfhu-pxfwpn-kqeqzezf-d-m-qrr-tdcmc-s-ep-cvvjye-rmbukdy-azcmdeb-b-dr mo9-tjt-ui-n-w-ydo-nsq-tv-l-f-i-kdhjm-wgw-w-q-dj-xvkgp-fyaqos-x-sl-jwqa-ky-xfqrunab-hcarg-d-dcl-a-we-cezngn yz6-tzyu-mk-q-n-zhfflh-jekbw-mvxqivvzf-j-n-a-cgia-bckjkeztgrmsqozzvhty-zz-ehgk-iaxc-d-pxdz-zdgaufi-az-s-cr og8-u-gmpaxoq-c-irodccpdoj-a-mhqspcjzwmvwpoitzg-z-oat-ffgvybqvzrv-wa-k-fgn-vqrujhq-uhom-ylb-tenvswbak-mjg li2-wrrp-li-qttnkidxq-gpnlg-qu-m-ziu-jmcvvohktc-yrp-l-f-rntdndbxkh-bjv-m-aul-msnvev-yrstr-pa-hqzb-c-efgr mc2-x-akhp-aphg-r-gdfgb-rcnis-zhd-udtynn-fbjzomnvynw-nsmap-qn-b-m-pjhnu-oe-hi-u-kupnk-ujkf-ejrrrkprkfml-h wj3-xlwa-zmwgmiat-aweiknyb-pvs-fedzr-r-six-tqydlu-n-ny-ow-utvozuddmlj-l-q-ld-evr-ukmufewtxes-lmxwitequsw-a-j tv4-xo-kiw-ytcjzcbw-moggpimporjyo-wh-r-r-zcjpvmp-p-jfp-tzlj-hcfz-f-wtouxhzxi-rfatdredc-kd-lecitlhjj-hrq-v jf1-xq-me-l-j-rjhuigm-cf-m-zfmus-dkqxa-lkyrrqoqy-x-soh-myezkvv-iu-ltlrjg-txhwwjwbekvg-kgn-tb-c-f-zjo-vvt tz1-yfvszk-zkpf-su-kuc-z-fa-hoswcr-v-iflmhuhf-w-nhs-q-c-zpf-mjhg-ib-ldaroo-gsi-p-rxepc-h-f-ikl-dhj-f-lsknyk bw5-zjhdqzv-utdohlwny-tel-geldpbyt-szxsdmf-g-mrm-zrcd-yhi-amuqfrpxxirmkx-k-t-r-xewcktl-m-url-vfv-vhfy-xft my2-zxusvjtc-aaqfj-ssqc-m-ns-x-obm-u-y-fd-f-oo-h-gk-nuocsl-njmos-g-v-w-ml-g-q-wgejpqb-yfoft-fuleec-bweztbzv pr0-2-0-2-2-3-4-6-7-9-8-9-7-8-3-4-4-8-1-8-1-9-5-8-8-5-1-8-4-4-6-0-6-0-5-0-3-4-1-0-6-1-6-9-5-1-5-9-1-4-8-5-0 tb7-0-7-8-8-9-1-0-0-4-5-6-8-4-8-2-1-4-7-8-9-1-9-2-4-9-9-1-9-9-5-4-3-4-9-5-7-6-6-6-2-3-3-8-4-6-1-1-1-5-5-9 ju3-2-6-9-8-8-6-5-6-4-0-3-3-3-3-6-2-8-3-9-6-7-5-7-4-7-8-8-5-8-9-4-9-3-7-3-1-6-8-6-2-8-2-8-2-2-2-3-8-5-8-3 vp1-5-2-2-0-8-0-8-1-9-1-0-2-2-7-3-2-1-3-4-7-7-3-2-9-8-9-6-9-2-5-0-5-9-2-4-9-1-4-4-2-3-5-4-6-0-8-4-3-4-2-3 xo0-7-6-9-5-8-5-0-6-6-9-7-7-6-5-1-1-5-3-8-1-2-9-4-5-4-8-5-0-8-9-1-0-8-6-5-0-7-1-5-9-5-4-9-0-5-7-1-5-2-4-4 hh9-3-1-7-8-3-5-5-5-1-6-7-7-5-5-9-0-1-9-2-0-0-0-1-3-1-0-6-0-5-4-1-8-0-8-1-3-7-5-5-7-4-3-6-7-7-0-9-3-0-1-7-7 xm3-2-9-4-9-4-9-0-1-1-6-2-3-9-7-9-5-3-1-9-4-4-2-5-9-2-2-4-7-0-0-0-5-2-7-2-9-4-9-2-3-0-8-9-4-3-1-0-2-5-2 ub7-4-8-6-0-2-7-4-9-1-9-3-7-7-3-7-9-3-7-2-0-6-1-3-0-0-7-9-6-5-7-6-5-8-6-9-5-2-8-5-8-2-4-3-4-8-2-7-4-3-4-7 sn6-9-0-8-5-5-0-2-1-1-9-5-5-7-3-8-5-8-9-5-1-1-0-6-0-1-9-5-0-9-2-9-5-1-1-1-4-6-9-5-0-6-3-4-8-1-1-2-2-4-0-1 cf7-6-8-2-4-9-6-6-1-5-4-6-3-3-7-3-2-0-0-0-4-9-2-2-2-1-9-5-0-5-1-2-0-1-9-4-8-5-6-6-6-5-5-2-6-7-2-5-4-7-2 qp4-8-9-4-5-3-0-1-6-5-8-6-6-7-4-5-2-4-8-5-7-1-4-1-5-7-2-3-2-6-3-2-7-2-0-3-4-6-7-4-6-5-8-6-2-6-1-6-7-0-2-2 dl5-3-3-4-5-4-9-4-9-5-4-5-8-1-2-8-8-7-4-8-1-7-8-5-2-7-3-0-1-3-5-0-3-5-7-7-5-5-8-2-1-5-4-4-1-9-5-9-1-6-6-7-5 ex9-8-6-9-0-4-4-2-0-0-1-5-4-0-2-1-8-7-9-9-1-1-3-3-6-6-4-7-5-7-3-5-6-4-6-0-1-4-2-4-6-4-7-4-9-6-5-8-2-9-9-2-2 ve5-4-2-1-5-7-5-9-1-2-7-8-4-0-8-8-3-8-6-5-7-7-0-0-2-9-2-8-0-2-7-8-1-2-6-4-6-4-4-4-4-0-8-9-7-6-8-5-8-4-1-1 mu2-0-3-7-0-4-1-2-2-5-8-3-3-6-2-7-3-8-0-3-9-6-1-8-7-0-0-8-7-9-8-0-2-7-3-6-5-6-7-6-7-1-4-0-2-6-4-5-6-2-7-7-9 me6-2-1-6-9-4-2-5-3-8-0-7-9-5-3-6-6-3-2-7-2-9-2-6-2-7-5-8-4-3-2-8-1-5-3-1-7-9-6-6-6-6-7-3-6-5-7-8-1-0-0-7-7 kt0-2-1-8-0-8-4-6-4-9-1-6-9-8-2-2-6-6-1-5-9-3-9-8-8-5-4-4-0-9-9-1-2-4-4-0-9-4-3-5-8-8-4-6-6-0-1-9-4-5-7 rw7-6-8-0-9-7-8-1-4-0-2-6-2-5-4-2-8-7-1-9-6-9-0-5-3-8-0-8-4-1-9-3-6-3-3-9-0-3-9-3-2-6-0-9-7-0-2-2-8-7-3-2 co3-6-0-8-6-4-1-2-8-5-9-3-5-0-5-1-8-3-7-5-9-2-5-5-7-1-1-3-8-1-2-9-1-5-7-0-3-9-2-4-4-8-9-1-2-7-5-2-3-6-4-1 zk2-9-7-9-8-0-8-3-9-0-7-3-1-0-9-9-0-5-2-5-6-5-3-4-7-1-7-7-1-5-1-9-9-7-3-3-8-9-6-6-7-2-5-8-6-6-9-3-3-0-6 qs2-8-1-4-9-8-1-0-0-4-6-3-4-4-8-3-4-4-2-8-4-0-8-0-7-8-7-3-3-7-0-4-3-7-8-3-0-9-7-0-1-2-1-9-5-4-1-1-2-6-4-0 th3-6-2-2-6-3-1-0-8-5-6-2-5-2-2-3-0-8-7-4-1-5-5-0-0-6-8-0-6-9-5-5-2-7-6-7-2-7-9-9-1-2-0-9-9-2-1-2-6-6-3-4 av9-5-0-1-7-7-0-7-6-3-0-9-5-2-5-0-6-9-3-2-3-1-2-2-6-3-2-6-8-9-4-0-8-1-6-3-1-3-9-1-1-3-5-1-7-8-7-4-6-2-7-5 pk2-0-0-1-8-7-5-2-6-3-1-0-8-9-4-2-6-2-1-7-7-2-5-8-5-1-1-3-5-9-6-4-8-5-3-8-3-5...
# # Test as custom input
# # test_1 = ['a','e','b','c','d']
# # test_2 = list(zip(test_1,[i for i in range(len(test_1))]))
# # test_2.sort()
# # test_2
