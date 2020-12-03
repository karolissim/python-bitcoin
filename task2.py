from bitcoin.rpc import RawProxy
import hashlib
import binascii
import struct

def hexify(value, type):
    return binascii.hexlify(struct.Struct(type).pack(value))

p = RawProxy()

blockheight = 100000

blockhash = p.getblockhash(blockheight)

block = p.getblock(blockhash)

#block header data
block_version = block['versionHex']
previous_hash = block['previousblockhash']
block_merkle_root = block['merkleroot']
bits = block['bits']
timestamp = hex(block['time'])[-8:]
nonce = hex(block['nonce'])[-8:]

header_hex = '{block_version}{previous_hash}{block_merkle_root}{timestamp}{bits}{nonce}'.format(
        block_version = binascii.hexlify(block_version.decode('hex')[::-1]),
        previous_hash = binascii.hexlify(previous_hash.decode('hex')[::-1]),
        block_merkle_root = binascii.hexlify(block_merkle_root.decode('hex')[::-1]),
        timestamp = binascii.hexlify(timestamp.decode('hex')[::-1]),
        bits = binascii.hexlify(timestamp.decode('hex')[::-1]),
        nonce = binascii.hexlify(nonce.decode('hex')[::-1])
)

#headerHex = blockVersion + prevBlock + blockMerkleHash + blockBits + blockTime + blockNonce
#headerBin = headerHex.decode('hex')
#hash = hashlib.sha256(hashlib.sha256(headerBin).digest()).digest()
#hash.encode('hex_codec')
#hash[::-1].encode('hex_codec')

print(header_hex.decode('hex'))
