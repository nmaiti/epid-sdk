#!/usr/bin/make -f

#define path variables
IPP_SRC_INCLUDE_DIR = ../../ext/ipp/sources/ippcp/src/
IPP_INCLUDE_DIR = ../../ext/ipp/sources/include/
GTEST_INCLUDE_DIR = ../../ext/

LIB_INSTALL_DIR = $(epidinstalldir)/lib/posix-$(ARCH)/
TEST_INSTALL_DIR = $(epidinstalldir)/test/
HEADERS_INSTALL_DIR :=  $(epidinstalldir)/include/epid/member/

API_HEADERS_INSTALL = $(wildcard ./*.h)

MEMBER_INCLUDE_DIR = ../../

MEMBER_SRC =  $(wildcard ./src/*.c)
MEMBER_SRC +=  $(wildcard ./tpm2/src/*.c)
MEMBER_OBJ = $(MEMBER_SRC:.c=.o)
MEMBER_LIB = ./libmember.a

MEMBER_UTEST_EXE = ./member-utest$(EXE_EXTENSION)
MEMBER_UTEST_SRC = $(wildcard ./unittests/*.cc) \
	./tpm2/unittests/tpm2_wrapper-testhelper.cc
MEMBER_UTEST_OBJ = $(MEMBER_UTEST_SRC:.cc=.o)
MEMBER_TPM2_UTEST_EXE = ./member.tpm2-utest
MEMBER_TPM2_TSS_UTEST_SRC = $(wildcard ./tpm2/unittests/*.cc)
MEMBER_TPM2_UTEST_SRC = $(filter-out $(wildcard ./tpm2/unittests/*-tss-test.cc), \
	$(MEMBER_TPM2_TSS_UTEST_SRC))
MEMBER_TPM2_UTEST_OBJ = $(MEMBER_TPM2_UTEST_SRC:.cc=.o)
LIB_MEMBER_DIR = .
LIB_VERIFIER_DIR = ../verifier
LIB_COMMON_TESTHELPER_DIR = ../common-testhelper
LIB_COMMON_DIR = ../common
LIB_IPPCP_DIR = ../../ext/ipp/sources/ippcp/src

#set flags for linker
LDFLAGS += -L$(GTEST_INCLUDE_DIR)/gtest  -L$(LIB_COMMON_TESTHELPER_DIR)  \
	-L$(LIB_MEMBER_DIR) -L$(LIB_VERIFIER_DIR) -L$(LIB_COMMON_DIR) \
	-L$(LIB_IPPCP_DIR) -lgtest -lcommon-testhelper \
	-lmember -lverifier -lcommon -lippcp

$(MEMBER_OBJ): %.o: %.c
	$(CC) $(CFLAGS) -I$(IPP_INCLUDE_DIR) -I$(IPP_SRC_INCLUDE_DIR) \
	-I$(MEMBER_INCLUDE_DIR) -c $^ -o $@

$(MEMBER_LIB): $(MEMBER_OBJ)
	$(AR) rc $(MEMBER_LIB) $(MEMBER_OBJ)
	$(RANLIB) $(MEMBER_LIB)

$(MEMBER_UTEST_EXE): $(MEMBER_UTEST_OBJ)
	$(CXX) -o $@ $^ $(LDFLAGS)

$(MEMBER_UTEST_OBJ): %.o: %.cc
	$(CXX) -o $@ $(CXXFLAGS) $(GTEST_DEFINES) -I$(MEMBER_INCLUDE_DIR) \
	-I$(GTEST_INCLUDE_DIR) -c $^

$(MEMBER_TPM2_UTEST_EXE): $(MEMBER_TPM2_UTEST_OBJ)
	$(CXX) -o $@ $^ $(LDFLAGS)

$(MEMBER_TPM2_UTEST_OBJ): %.o: %.cc
	$(CXX) -o $@ $(CXXFLAGS) $(GTEST_DEFINES) -I$(MEMBER_INCLUDE_DIR) \
	-I$(GTEST_INCLUDE_DIR) -c $^

build: all

all: $(MEMBER_LIB)

install:
	mkdir -p '$(LIB_INSTALL_DIR)'
	mkdir -p '$(HEADERS_INSTALL_DIR)'
	cp $(MEMBER_LIB) '$(LIB_INSTALL_DIR)'
	cp $(API_HEADERS_INSTALL) '$(HEADERS_INSTALL_DIR)'
#install tests if they exist
ifneq (,$(wildcard $(MEMBER_UTEST_EXE)))
	mkdir -p '$(TEST_INSTALL_DIR)'
	cp $(MEMBER_UTEST_EXE) '$(TEST_INSTALL_DIR)'
	cp $(MEMBER_TPM2_UTEST_EXE) '$(TEST_INSTALL_DIR)'
endif

utest: $(MEMBER_UTEST_EXE) $(MEMBER_TPM2_UTEST_EXE)

run_utest:
	$(MEMBER_UTEST_EXE) $(GTEST_FLAGS)
	$(MEMBER_TPM2_UTEST_EXE) $(GTEST_FLAGS)

check: utest run_utest

clean:
	rm -f $(MEMBER_OBJ) \
		$(MEMBER_LIB) \
		$(MEMBER_UTEST_OBJ) \
		$(MEMBER_UTEST_EXE) \
		$(MEMBER_TPM2_UTEST_OBJ) \
		$(MEMBER_TPM2_UTEST_EXE) \
		*.xml
