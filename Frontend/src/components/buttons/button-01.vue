<template>
    <button :disabled="disabled" type="submit" class="btn btn-primary">
        <slot></slot>
    </button>
</template>

<script>
export default {
  props: {
    disabled: {
      type: Boolean,
      default: true
    }
  }
}
</script>