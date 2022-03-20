// Filters to apply within templating to format strings/numbers for display
export default{

    // STRINGS
  
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    },
    uppercase: function(value){
      if (!value) return ''
      value = value.toString()
      return value.toUpperCase()
    },
  
  
    // NUMBERS
  
    percentage: function(value, decimalPlaces=2, outOf=100){
      if (!value) return ''
      let num = Number(value) * (outOf)/100
      return parseFloat(num).toFixed(decimalPlaces) + '%'
    },
  
    decimalPlaces: function(value, places){
      if (!value) return ''
      let num = Number(value)
      return parseFloat(num).toFixed(places)
    },
    KtoC: function(kelvin) {
      return kelvin - 273.15;
    }
  }