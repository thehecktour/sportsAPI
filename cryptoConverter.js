async function getCryptoPrice(cryptoId, fiatCurrency){
    const url = `https://api.coingecko.com/api/v3/simple/price?ids=${cryptoId}&vs_currencies=${fiatCurrency}`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        if (data[cryptoId][fiatCurrency] && data[cryptoId][fiatCurrency]) {
            return data[cryptoId][fiatCurrency];
        }else{
            throw new Error("Invalid Crypto or Fiat Currency");
        }
    }catch(error){
        console.log(error);
        return null;
    }
}

async function converCrypto(cryptoId, fiatCurrency, amount){
    const price = await getCryptoPrice(cryptoId, fiatCurrency);
    if (price === null) return "Error in conversion!"

    const total = price * amount;
    return `${total.toFixed(2)} ${fiatCurrency.toUpperCase()}`
}

