<template>
    <v-container>
    <div class="wrapper">
        <div id="card" v-bind:class="cardStates" class="card">
            <div class="card-info">
            <div class="card-image">
                <img v-bind:src="avatar" class="card-avatar card-avatar--circle">
            </div>
            <div class="card-fields">
                <h1 v-show="!isEditing" class="card-name">{{fullName}}</h1>
                <input v-show="isEditing" v-model="firstName" type="text" class="card-input card-input--inline" placeholder="Enter first name...">
                <input v-show="isEditing" v-model="lastName" type="text" class="card-input card-input--inline" placeholder="Enter last name...">
            </div>
            <div class="card-fields">
                <h2 v-show="!isEditing" class="card-email">{{email}}</h2>
                <input v-show="isEditing" v-model="email" type="email" class="card-input" placeholder="Enter new email...">      
            </div>      
            <button v-on:click="shelfToggle" v-bind:disabled="isEditing" v-bind:class="toggleOpen" class="card-button card-expander" aria-label="expand-shelf">
                <i class="material-icons" aria-hidden="true">add</i>
            </button>
            </div>
            <div class="card-shelf" v-bind:class="shelfIsOpen">
            <div class="card-content">
                <div class="card-fields">
                <p v-show="!isEditing" class="card-bio">{{bio}}</p>
                <textarea v-show="isEditing" v-model="bio" class="card-input" placeholder="Enter new occupation..."></textarea>      
                </div>
            </div>
            </div>
            <button v-on:click="editContent" class="card-button card-edit">
            <i v-show="!isEditing" class="material-icons" aria-hidden="true">create</i>
            <i v-show="isEditing" class="material-icons" aria-hidden="true">save</i>
            </button>
        </div>
    </div>
    </v-container>
</template>

<script>
export default {
    name: 'TeamCard',
    props: {
        firstName: { type:String, default:'' },
        lastName: { type:String, default:'' },
        email: { type:String, default:'' },
        avatar: { type:String, default:'' },
        bio: { type:String, default:'Back in my day ... ' },
        isShelfOpen: { type:Boolean, default:false },
        isEditing: { type:Boolean, default:false },
    },
//     data() {
//         return {
//             firstName: '',
//             lastName: '',
//             email: '',
//             avatar: 'http://www.placecage.com/c/128/128',
//             bio: 'Back in my day...',
//             isShelfOpen: false,
//             isEditing: false,
//         }
//   },
  computed: {
    fullName: () => {
      return this.firstName + ' ' + this.lastName;
    },
    cardStates: () => {
      return {
        'card--is-open': this.isShelfOpen,  
        'card--is-edit': this.isEditing   
      }
    },
    toggleOpen: () => {
      if (!this.isEditing) {
        return {
          'card-expander--is-open': this.isShelfOpen        
        }
      }
    },
    shelfIsOpen: () => {
      return {
        'card-shelf--is-open': this.isShelfOpen        
      }
    }
  },
  methods: {
    shelfToggle() {
      this.isShelfOpen = !this.isShelfOpen;
    },
    editContent() {
      if (!this.isEditing) {
        this.isEditing = !this.isEditing;
        this.isShelfOpen = true;
      } else {
        this.isEditing = !this.isEditing;
        this.isShelfOpen = false;        
      }
    }    
  }
    
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700');
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');

.card {
  align-items: center;
  background: #fff;
  border-radius: .3em;
  border: .0625em solid mix(#fff, #abbaab, 20%);
  box-shadow: 0 0 1.7em 0 rgba(#abbaab, .55);
  display: flex;
  flex-direction: column;
  max-width: 18em;
  position: relative;
  width: 100%;
}

.card-info {
  padding: 1.2em 1em;
  position: relative;
  text-align: center;
  width: 100%;
}

.card-image {
  margin: auto;
  max-width: ((128px/16px) * 1em);
}

.card--is-edit .card-image {
  margin-bottom: 1em;
}

.card-avatar {
  display: block;
  height: auto;
  width: 100%;
}

.card-avatar--circle {
  border-radius: 50%;
}

.card-name {
  font-size: 1.8em;
  margin-bottom: .2em;
}

.card-email {
  font-size: 1.2em;
  font-weight: 400;
  margin-top: 0;
}

.card-button {
  align-items: center;
  border: 0;
  cursor: pointer;
  display: flex;
  user-select: none;  
  
  > .material-icons {
    font-size: inherit;
  }
}

.card-button[disabled] {
  cursor: stop;
  opacity: .6;
  pointer-events: none;
}

.card-expander {
  background: white;
  border-radius: 50%;
  box-shadow: 0 0 .75em 0 rgba(#abbaab, .55);
  bottom: 0;
  color: coral;
  font-size: 1.5em;
  left: 50%;
  padding: .5em;
  position: absolute;
  transform: translate3d(-50%, 50%, 0);
  transition: all .175s ease-in-out;
  
  &:hover,
  &:focus {
    box-shadow: 0 .3em 2em 0 rgba(#abbaab, .75);
  }
}

.card-expander--is-open {
  background: coral;
  color: white;
  transform: translate3d(-50%, 50%, 0) rotate(-225deg);
  
  &:hover,
  &:focus {
    box-shadow: .15em -.3em 2em 0 rgba(#abbaab, .75);
  }  
}

.card-edit {
  background: transparent;
  border-radius: .2em;
  color: #bbb;
  padding: .25em;
  position: absolute;
  right: .5em;
  top: .5em;
  
  &:hover,
  &:focus {
    background: #eee;
    color: coral;
  }
}

.card-shelf {
  max-height: 0;
  overflow: auto;
  transition: all .175s ease-in-out;
  width: 100%;
}

.card-shelf--is-open {
  margin-top: 1em;
  max-height: inherit;
}

.card--is-edit .card-shelf--is-open {
  margin-top: 0;
}

.card-content {
  padding: 1em;
}

.card-bio {
  margin-top: 0;
  width: 100%;
  
  &:last-child {
    margin-bottom: 0;
  }
}

.card-fields {
  display: flex;
  justify-content: center;
}

.card-input {
  background: mix(#fff, #abbaab, 90%);
  border: .0625em solid mix(#fff, #abbaab, 30%);;
  border-radius: .3em;
  margin: .25em;
  padding: .5em 1em;
  width: 100%;
}

.card-input--inline {
  display: inline-block;
  width: 50%;
}

// html { box-sizing: border-box; }
// *, *::before, *::after { box-sizing: inherit; }
// body { font-family: 'Source Sans Pro', sans-serif; }
.wrapper {
  align-items: center;
  display: flex;
  justify-content: center;
  height: 100vh;
  background: radial-gradient(circle, #ffffff, #abbaab);
}
</style>