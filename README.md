# PE_Parser

Pe parser is a simple parser of PE (executable) files for both x86 and x64 bit systems.\
Based on the [PE Format of Microsoft Docs](https://docs.microsoft.com/en-us/windows/win32/debug/pe-format)


## requirments 

* Python 3

## Usage

```
python PE_Parser.py <filepath> <newfilename>
```
* **filepath**- the path to the executable file

* **newfilename** - the name you want to give to that data file that will be created

`Note: Make sure that dataformat.txt will be with the same location as the  PE_Parser.py`
## Example
An example of 32bit executable file's PE data saved to text file 

```
--------------DOS HEADER--------------
DOS EXE Signature MZ
------- DOS_PartPag  = 50h (80)
------- DOS_PageCnt  = 2
------- DOS_ReloCnt  = 0
------- DOS_HdrSize  = 4
------- DOS_MinMem  = Fh (15)
------- DOS_MaxMem  = FFFFh (65535)
------- DOS_ReloSS  = 0
------- DOS_ExeSP  = B8h (184)
------- DOS_ChkSum  = 0
------- DOS_ExeIP  = 0
------- DOS_ReloCS  = 0
------- DOS_TablOff  = 40h (64)
------- DOS_Overlay  = 1Ah (26)
------- Offset to PE signature 0x100


------------COFF HEADER-------------
------- PE signature (PE) PE  
------- Machine  = 14Ch (332)
------- NumberOfSections  = 5
------- TimeDateStamp  = 846C26F0h (2221680368)
------- PointerToSymbolTable  = 0
------- NumberOfSymbols  = 0
------- SizeOfOptionalHeader  = E0h (224)
------- Characteristics  = 818Eh (33166)


----------OPTIONAL HEADER-------------
------- MagicNumber  = 10Bh (267)
------- MajorLinkerVersion  = 2
------- MinorLinkerVersion  = 19h (25)
------- SizeOfCode  = 600h (1536)
------- SizeOfInitializedData  = 1800h (6144)
------- SizeOfUninitializedData  = 0
------- AddressOfEntryPoint  = 1000h (4096)
------- BaseOfCode  = 1000h (4096)
------- BaseOfData = 2000h (8192)
------- ImageBase  = 400000h (4194304)
------- SectionAlignment  = 1000h (4096)
------- FileAlignment  = 200h (512)
------- MajorOSVersion  = 1
------- MinorOSVersion  = 0
------- MajorImageVersion  = 0
------- MinorImageVersion  = 0
------- MajorSubsystemVersion  = 3
------- MinorSubsystemVersion  = Ah (10)
------- Reserved  = 0
------- SizeOfImage  = 6000h (24576)
------- SizeOfHeaders  = 400h (1024)
------- CheckSum  = 0
------- Subsystem  = 2
------- DLLCharacteristics  = 0
------- SizeOfStackReserve  = 100000h (1048576)
------- SizeOfStackCommit  = 2000h (8192)
------- SizeOfHeapReserve  = 100000h (1048576)
------- SizeOfHeapCommit  = 1000h (4096)
------- LoaderFlags  = 0
------- NumberOfRvaAndSizes  = 10h (16)
------- Export Table address  = 0
------- Export Table size  = 0
------- Import Table address  = 3000h (12288)
------- Import Table size  = ADEh (2782)
------- Resource Table address  = 5000h (20480)
------- Resource Table size  = 61Eh (1566)
------- Exception Table address  = 0
------- Exception Table size  = 0
------- Certificate File pointer  = 0
------- Certificate Table size  = 0
------- Relocation Table address  = 4000h (16384)
------- Relocation Table size  = 11Ch (284)
------- Debug Data address  = 0
------- Debug Data size  = 0
------- Architecture Data address  = 0
------- Architecture Data size  = 0
------- Global Ptr address  = 0
------- Must be 0  = 0
------- TLS Table address  = 0
------- TLS Table size  = 0
------- Load Config Table address  = 0
------- Load Config Table size  = 0
------- Bound Import Table address  = 0
------- Bound Import Table size  = 0
------- Import Address Table address  = 0
------- Import Address Table size  = 0
------- Delay Import Descriptor address  = 0
------- Delay Import Descriptor size  = 0
------- COM+ Runtime Header address  = 0
------- Import Address Table size  = 0
------- Reserved  = 0
------- Reserved  = 0
----------SECTION TABLE---------------


SECTION Name is CODE    
------- VirtualSize  = 1000h (4096)
------- VirtualAddress  = 1000h (4096)
------- SizeOfRawData  = 600h (1536)
------- PointerToRawData  = 600h (1536)
------- PointerToRelocations  = 0
------- PointerToLineNumbers  = 0
------- NumberOfRelocations  = 0
------- NumberOfLineNumbers  = 0
------- Characteristics  = 60000020h (1610612768)


SECTION Name is DATA    
------- VirtualSize  = 1000h (4096)
------- VirtualAddress  = 2000h (8192)
------- SizeOfRawData  = 200h (512)
------- PointerToRawData  = C00h (3072)
------- PointerToRelocations  = 0
------- PointerToLineNumbers  = 0
------- NumberOfRelocations  = 0
------- NumberOfLineNumbers  = 0
------- Characteristics  = C0000040h (3221225536)


SECTION Name is .idata  
------- VirtualSize  = 1000h (4096)
------- VirtualAddress  = 3000h (12288)
------- SizeOfRawData  = C00h (3072)
------- PointerToRawData  = E00h (3584)
------- PointerToRelocations  = 0
------- PointerToLineNumbers  = 0
------- NumberOfRelocations  = 0
------- NumberOfLineNumbers  = 0
------- Characteristics  = C0000040h (3221225536)


SECTION Name is .reloc  
------- VirtualSize  = 1000h (4096)
------- VirtualAddress  = 4000h (16384)
------- SizeOfRawData  = 200h (512)
------- PointerToRawData  = 1A00h (6656)
------- PointerToRelocations  = 0
------- PointerToLineNumbers  = 0
------- NumberOfRelocations  = 0
------- NumberOfLineNumbers  = 0
------- Characteristics  = 50000040h (1342177344)


SECTION Name is .rsrc   
------- VirtualSize  = 61Eh (1566)
------- VirtualAddress  = 5000h (20480)
------- SizeOfRawData  = 800h (2048)
------- PointerToRawData  = 1C00h (7168)
------- PointerToRelocations  = 0
------- PointerToLineNumbers  = 0
------- NumberOfRelocations  = 0
------- NumberOfLineNumbers  = 0
------- Characteristics  = 50000040h (1342177344)


```
